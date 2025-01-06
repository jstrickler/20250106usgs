import os
from git import Git, Repo

github_url = 'https://github.com/jstrickler/myproject.git'

home_dir = os.path.expanduser('~')
source_repo_dir = os.path.join(home_dir, 'myproject')
local_clone_dir = os.path.join(home_dir, 'myproject_local')
remote_clone_dir = os.path.join(home_dir, 'myproject_remote')

repo = Repo(source_repo_dir)

Repo.clone_from(source_repo_dir, local_clone_dir)  # Clone existing local repo to new repo
Repo.clone_from(github_url, remote_clone_dir)  # Same, from remote

