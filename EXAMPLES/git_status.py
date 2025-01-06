import os
from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')  # Folder of repository

repo = Repo(repo_dir)   # Create Repo object

os.chdir(repo_dir)  # Go to repo folder (not always required)

g = Git(repo)   # Create Git() object; this is used for most git commands
print(g.status())  # Get status


