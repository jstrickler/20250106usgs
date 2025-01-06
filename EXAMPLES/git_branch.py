import os
import shutil

from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'myproject')

repo = Repo(repo_dir)

# get current (EXAMPLES) dir before changing to repo dir
example_dir = os.getcwd()

os.chdir(repo_dir)

# simulate creating a file in the project
file_to_add = 'tyger.py'
file_to_add_source = os.path.join(os.path.dirname(example_dir), file_to_add)
shutil.copy(file_to_add_source, ".")  

g = Git(repo)

g.checkout('-b', 'myfeature')  # Create new branch named "myfeature"

g.add('tyger.py')  # tyger.py is only added and committed to branch "myfeature", not main branch
g.commit('tyger.py', message='new file')

