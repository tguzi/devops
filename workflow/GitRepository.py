import os
from git.repo import Repo
from git.repo.fun import is_git_dir

"""
git仓库管理
"""


class GitRepository(object):
    def __init__(self, local_dir, repo_url, branch='master'):
        self.local_path = local_dir
        self.repo_url = repo_url
        self.repo = None
        self.origin = None
        self.initial(repo_url, branch)

    def initial(self, repo_url, branch):
        """
        初始化git仓库
        :param repo_url:
        :param branch:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    def pull(self):
        """
        从线上拉最新代码
        :return:
        """
        self.repo.git.pull()

    def fetch(self):
        """
            fetch操作
        """
        self.repo.remote.fetch()

    def branches(self):
        """
        获取所有分支
        :return:
        """
        branches = self.repo.remote().refs
        return [item.remote_head for item in branches if item.remote_head not in ['HEAD', ]]

    def commits(self):
        """
        获取所有提交记录
        :return:
        """
        commit_log = self.repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
                                       max_count=50,
                                       date='format:%Y-%m-%d %H:%M')
        log_list = commit_log.split("\n")
        return [eval(item) for item in log_list]

    def tags(self):
        """
        获取所有tag
        :return:
        """
        return [tag.name for tag in self.repo.tags]

    def change_to_branch(self, branch):
        """
        切换分支
        :param branch:
        :return:
        """
        self.repo.git.checkout(branch)

    def change_to_commit(self, branch, commit):
        """
        切换commit
        :param branch:
        :param commit:
        :return:
        """
        self.change_to_branch(branch=branch)
        self.repo.git.reset('--hard', commit)

    def change_to_tag(self, tag):
        """
        切换tag
        :param tag:
        :return:
        """
        self.repo.git.checkout(tag)

    def create_remote_branch(self, branch):
        """
            创建远程分支
        """
        try:
            self.repo.git.checkout('HEAD', b=branch)
            # 把本地分支推送到远程
            self.repo.git.push('origin', branch)
        except Exception as err:
            return err.__str__()

    def merge_and_push(self, target, origins):
        """
            合并分支，并且推送
        """
        try:
            self.repo.git.checkout(target)
            self.repo.git.fetch()
            for origin in origins:
                self.repo.git.merge(origin)
            self.repo.git.push('origin', target)
        except Exception as err:
            return err.__str__()

    def delete_remote_branches(self, branches):
        """
        批量删除远程分支
        """
        repo_remote = self.repo.remote(name='origin')
        # 校验是否有远程分支
        for repo_branch in self.repo.references:
            if repo_branch.name in branches:
                print("deleting remote branch: %s" % repo_branch)
                repo_remote.push(refspec=(":%s" % repo_branch))


if __name__ == '__main__':
    local_path = os.path.join('codes', 't1')
    repo = GitRepository(local_path, '')
    branch_list = repo.branches()
    repo.change_to_branch('master')
    repo.pull()
