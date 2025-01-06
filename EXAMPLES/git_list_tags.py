import os
from git import Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')

repo = Repo(repo_dir)

for tag in repo.tags:  # Iterate over all tags for repo
    print(tag.name)
