from fabric.api import local

def prepare_deploy():
    local("python test.py")
    local("git add -p && git commit --allow-empty")
    local("git push")