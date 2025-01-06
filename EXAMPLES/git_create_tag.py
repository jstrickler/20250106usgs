import os
from git import Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')

repo = Repo(repo_dir)

# Create tag with descriptive message
repo.create_tag("v1.0.0", message="First Public Release")

