## 安装


## 使用‌

* 初始化: git flow init
* 开始新Feature: git flow feature start MYFEATURE
* Publish一个Feature(也就是push到远程): git flow feature publish MYFEATURE
* 获取Publish的Feature: git flow feature pull origin MYFEATURE
* 完成一个Feature: git flow feature finish MYFEATURE
* 开始一个Release: git flow release start RELEASE [BASE]
* Publish一个Release: git flow release publish RELEASE
* 发布Release: git flow release finish RELEASE 别忘了git push --tags
* 开始一个Hotfix: git flow hotfix start VERSION [BASENAME]
* 发布一个Hotfix: git flow hotfix finish VERSION
