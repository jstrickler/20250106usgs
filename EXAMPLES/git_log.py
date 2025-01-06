import os
from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')

repo = Repo(repo_dir)

os.chdir(repo_dir)

g = Git(repo)
print(g.log())  # get log for entire repo
print('-' * 60)
print(g.log('spam.py'))  # get log for specific file
print('-' * 60)
print(g.log('eggs.py'))  # get log for specific file
