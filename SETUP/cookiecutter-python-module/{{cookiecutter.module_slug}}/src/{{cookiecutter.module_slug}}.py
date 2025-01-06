"""
Module documentation...
"""
{% if cookiecutter.has_scripts == 'y' %}
import sys
{% endif  %}

{% if cookiecutter.has_scripts == 'y' %}
# this is the function providing the 'actual' script
# you can also import this module normally and use this function 
{% endif %}
def sample_function(*args):
    """
    Sample function documentation...
    """
    print("sample {{cookiecutter.module_slug}} function")

{% if cookiecutter.has_scripts == 'y' %}
# this is a wrapper that is used to create the callable cli version of the function
def _sample_function_cli():  # name can be anything
    # access sys.argv as needed (copied from script's args)
    args = sys.argv[1:]
    print(f"Args to script: {args}")  # diagnostic -- delete
    sample_function(*args)  # call the 'real' function
    # note: change '*args' to actual params needed

#  in pyproject.toml, add this section
#
#  [scripts]
#  script_name = '{{cookiecutter.module_slug}}:_sample_function_cli'
#
# then you can run my_script_name from the command line

{% else %}

class {{cookiecutter.module_slug | title}}:
    """
    Class documentation...
    """

    def sample_method(self):
        """
        Sample method documentation...
        """
        print("sample {{cookiecutter.module_slug | title}} instance method")

{% endif %}

if __name__ == "__main__":
    # the code in this block (and all the code above) will be run when
    # either
    #    python {{cookiecutter.module_slug}}.py
    # or 
    #    python -m {{cookiecutter.module_slug}}
    # is executed, but NOT when imported like
    #    import {{cookiecutter.module_slug}}
    print(f"Hello from {__file__}")
