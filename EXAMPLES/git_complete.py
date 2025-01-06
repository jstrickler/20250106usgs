import os
import shutil
from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir = os.path.join(home_dir, 'otherproject')

r = Repo.init(repo_dir)  # Create new empty repo
example_dir = os.getcwd()

os.chdir(repo_dir)

file_to_add = 'pastable.py'
file_to_add_source = os.path.join(os.path.dirname(example_dir), file_to_add)
g = Git(r)  # Create Git() object from repo

# Copy file to add (typically created with IDE, so no need to copy)
shutil.copy(file_to_add_source, ".")  

g.add(file_to_add)  # Stage file for commit
g.commit(file_to_add, message="initial commit")  # Commit file
print(g.log())  # Show repo log
