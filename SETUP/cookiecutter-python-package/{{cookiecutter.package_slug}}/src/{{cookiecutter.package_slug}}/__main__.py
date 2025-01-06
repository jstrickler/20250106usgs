import sys
from {{cookiecutter.package_slug}}.{{cookiecutter.module_slug}} import sample_function

# this is executed when package is called like
#    python -m {{cookiecutter.package_slug}} 
def main(*args):
    print("In main of {{cookiecutter.package_slug}}")
    sample_function(*args)


if __name__ == "__main__":
    args = sys.argv[1:]  # get args; skip script name
    main(*args)  # call main() defined above