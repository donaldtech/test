import git
import os
import shutil

URL_OF_GIT_REPO = 'git@github.com:donaldtech/test.git'
PATH_OF_GIT_REPO = './tmp_helm'


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def git_push():
    if os.path.exists(PATH_OF_GIT_REPO):
        shutil.rmtree(PATH_OF_GIT_REPO)
    try:
        repo = git.Repo.clone_from(url=URL_OF_GIT_REPO, to_path=PATH_OF_GIT_REPO)
        copy_and_overwrite('./mydir', PATH_OF_GIT_REPO + '/mydir')
        repo.git.add(update=True)
        commit_msg = '[CI SKIP] update according to %s' % repo.head.commit
        repo.index.commit(commit_msg)
        origin = repo.remote(name='origin')
        origin.pull()
        repo.git.commit("--amend", commit_msg)
        origin.push()
    except:
        print('Some error occured while pushing the code')   
    finally:
        shutil.rmtree(PATH_OF_GIT_REPO)

# https://note.qidong.name/2018/01/gitpython/

