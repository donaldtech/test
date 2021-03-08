import git
import os
import shutil

DEPLOY_REPO = 'git@github.com:donaldtech/deployment.git'
DEPLOY_PATH = './helm_deployment'


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def git_push():
    if os.path.exists(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
    try:
        repo = git.Repo.clone_from(url=DEPLOY_REPO, to_path=DEPLOY_PATH)
        copy_and_overwrite('./mydir', DEPLOY_PATH + '/mydir')
        repo.git.add('--all')
        commit_msg = 'update according to %s ' os.getenv('COMMIT_ID', 'latest commit')
        repo.index.commit(commit_msg)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')   
    finally:
        shutil.rmtree(DEPLOY_PATH)
