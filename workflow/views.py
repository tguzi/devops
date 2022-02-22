import os

from django.http import JsonResponse

from workflow.GitRepository import GitRepository
from workflow.models import Env

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


def init(request):
    if request.method == 'GET':
        env_list = Env.objects.all().values()
        successRes['data'] = list(env_list)
        # print(devops_git.change_to_branch())
        return JsonResponse(successRes, content_type='application/json')
    else:
        return JsonResponse(errRes)


# 添加环境
def add_env(request):
    print(request.method)
    if request.method == 'POST':
        branch = request.POST.get('branch')
        name = request.POST.get('name')
        env = request.POST.get('env')
        Env.objects.create(branch=branch, name=name, env=env)
        successRes['data'] = 'success'
        successRes['msg'] = '操作成功'
        return JsonResponse(successRes, content_type='application/json')
    else:
        errRes['msg'] = '请求方式不对'
        return JsonResponse(errRes)
