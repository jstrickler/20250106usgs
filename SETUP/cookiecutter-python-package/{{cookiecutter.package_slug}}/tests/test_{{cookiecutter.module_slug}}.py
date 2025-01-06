import pytest
{% set module_class = cookiecutter.module_slug.split('_')|map('capitalize')|join %}
from {{cookiecutter.package_slug}}.{{cookiecutter.module_slug}} import sample_function
{% if cookiecutter.has_scripts != 'y'-%}
from {{cookiecutter.package_slug}}.{{cookiecutter.module_slug}} import {{ module_class }}

@pytest.fixture
def {{cookiecutter.module_slug | title}}_object():
    return {{module_class}}()

def test_{{cookiecutter.module_slug | title}}_instance_has_sample_method({{cookiecutter.module_slug | title}}_object):
    assert hasattr({{cookiecutter.module_slug | title}}_object, "sample_method")

{% endif %}

def test_{{cookiecutter.module_slug}}_has_sample_function():
    assert sample_function() is None  # no return value
