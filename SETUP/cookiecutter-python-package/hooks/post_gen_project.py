import sys
import os
from subprocess import run

print("Installing module in editable mode")
run([sys.executable, '-m', 'pip', 'install', '-e', '.'])
print()
print("""
Add your code to module src/{{cookiecutter.package_slug}}/{{cookiecutter.module_slug}}.py.

Add more modules or subpackages to src/{{cookiecutter.package_slug}}


The following tasks may be run from the command line in the project (top level) folder:

Run all tests:
    pytest
   
Generate documentation:
    cd docs
    make latexpdf

    or
    
    cd docs
    make html
    
""")

if "{{cookiecutter.has_main}}" != "y":
    dunder_main_path = "src/{{cookiecutter.package_slug}}/__main__.py"
    if os.path.exists(dunder_main_path):
        os.remove(dunder_main_path)
