import json
import os
from django.http import JsonResponse
import datetime
from django.db.models.functions import Lower, TruncDate
from django.views.decorators.http import require_http_methods
from workflow.GitRepository import GitRepository
from workflow.models import Env, Demand, RelationDemandEnv

# 返回结果
errRes = {
    "status": "0",
    "data": "",
    "msg": "操作失败",
}
successRes = {
    "status": "0",
    "data": "",
    "msg": "操作成功",
}

local_path = os.path.abspath(os.path.join(os.getcwd(), "../../code"))

repo_path = 'https://github.com/tguzi/devops.git'

devops_git = GitRepository(local_path, repo_path)


def getBranchName(prefix='feature'):
    """
        获取分支名称
        分支格式 feature-YYYY-MM-DD-HH-mm-ss
    """
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    branch_name = f'{prefix}-{now_time}'
    return branch_name


@require_http_methods(['GET'])
def init(request):
    try:
        env_str = request.GET.get('env', 'test')
        # 获取列表信息
        env_info = Env.objects.filter(env=env_str).values()[0]
        demand_list = Demand.objects.all().values()
        integrated_list = RelationDemandEnv.objects.filter(env_id=env_info['id']).values(
            description=Lower('demand__description'),
            tester=Lower('demand__tester'),
            branch=Lower('demand__branch'),
            developer=Lower('demand__developer'),
            publish_time=TruncDate('demand__publishTime'),
            demandId=Lower('demand_id'),
            envId=Lower('env_id'),
            envName=Lower('env__name'),
            envBranch=Lower('env__branch'),
        )
        if not env_info['branch']:
            # 没有分支时，创建分支
            branch_name = getBranchName('release')
            GitRepository.create_remote_branch(devops_git, branch_name)
            env_info['branch'] = branch_name
            Env.objects.filter(env=env_str).update(branch=branch_name)
        env_info['demands'] = list(demand_list)
        env_info['integratedList'] = list(integrated_list)
        successRes['data'] = env_info
        return JsonResponse(successRes, content_type='application/json')
    except Exception as err:
        print(err)
        return JsonResponse(errRes)


# 添加需求
@require_http_methods(['POST'])
def add_demand(request):
    try:
        publish_time = request.POST.get('publishTime')
        description = request.POST.get('description')
        developer = request.POST.get('developer')
        tester = request.POST.get('tester')
        branch_name = request.POST.get('branch_name')
        print('branch_name', branch_name)
        GitRepository.create_remote_branch(devops_git, branch_name)
        Demand.objects.create(
            publishTime=publish_time,
            description=description,
            branch=branch_name,
            developer=developer,
            tester=tester,
        )
        successRes['data'] = 'success'
        successRes['msg'] = '操作成功'
        return JsonResponse(successRes)
    except Exception as err:
        print(err)
        return JsonResponse(errRes)


# 删除需求
@require_http_methods(['DELETE'])
def delete_demand(request):
    try:
        demand_id = request.GET.get('id')
        Demand.objects.filter(id=demand_id).delete()
        return JsonResponse(successRes)
    except Exception as err:
        print(err)
        return JsonResponse(errRes)


# 添加环境
@require_http_methods('POST')
def add_env(request):
    branch = request.POST.get('branch')
    name = request.POST.get('name')
    env = request.POST.get('env')
    print('add env', request.POST)
    Env.objects.create(branch=branch, name=name, env=env)
    successRes['data'] = 'success'
    successRes['msg'] = '操作成功'
    return JsonResponse(successRes, content_type='application/json')


# 加入集成
@require_http_methods(['POST'])
def add_integration(request):
    try:
        env_branch = request.POST.get('envBranch')
        env_id = request.POST.get('envId')
        demand_branch = request.POST.get('demandBranch')
        demand_id = request.POST.get('demandId')
        GitRepository.merge_and_push(devops_git, env_branch, demand_branch)
        RelationDemandEnv.objects.create(demand_id=demand_id, env_id=env_id)
        return JsonResponse(successRes)
    except Exception as err:
        errRes['data'] = err.__str__()
        return JsonResponse(errRes)


# 退出集成
@require_http_methods(['POST'])
def exit_integration(request):
    try:
        env_id = request.POST.get('envId')
        demand_id = request.POST.get('demandId')
        # 删除关系
        RelationDemandEnv.objects.filter(env_id=env_id, demand_id=demand_id).delete()
        # 更新集成信息
        new_branch = getBranchName('release')
        Env.objects.filter(id=env_id).update(branch=new_branch)
        # 现有的集成
        env_demand_list = RelationDemandEnv.objects.filter(env_id=env_id).values_list('demand__branch', flat=True)
        GitRepository.merge_and_push(devops_git, new_branch, env_demand_list)
        return JsonResponse(successRes)
    except Exception as err:
        errRes['data'] = err.__str__()
        return JsonResponse(errRes)


@require_http_methods(['GET'])
def test(request):
    """
    测试方法用
    """
    env = request.POST.get('env', 'test')
    # branch = request.POST.get('branch', 'feature/test')
    # env_info = Env.objects.filter(env=env).first()
    # if not env_info.demands:
    #     demands = branch
    # else:
    #     demands = env_info.demands.split(",")
    #     demands.append(branch)
    #     demands = ",".join(demands)
    env_demand_list = RelationDemandEnv.objects.filter(env_id=1).values_list('demand__branch', flat=True)
    for demand in env_demand_list:
        print('demand: ', env_demand_list, type(demand[0]))
    # print(devops_git.change_branch_and_push('feature-202203022344'))
    # devops_git.change_branch_and_push('feature/test')
    # devops_git.merge_and_push('master', 'feature/test-0302')
    # devops_git.delete_remote_branches(['feature/test-0302'])
    # print(devops_git.branches())
    return JsonResponse(successRes)
