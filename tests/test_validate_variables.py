

import pytest
import jinja2
from creator.validate_variables import VariableValidator

import os

@pytest.fixture
def prepare_input():
    file_input = {
        'template_file': 'tests/resources/sample_template.jinja2',
        'config_file': 'tests/resources/sample_config.yml'
    }

    return file_input

@pytest.fixture
def prepare_wrong_input():
    file_input = {
        'template_file': 'tests/resources/sample_template.jinja2',
        'config_file': 'tests/resources/sample_error_config.yml'
    }

    return file_input

@pytest.fixture
def prepare_missing_template_file():
    file_input = {
        'template_file': 'tests/resources/missing_template.jinja2',
        'config_file': 'tests/resources/sample_error_config.yml'
    }

    return file_input

@pytest.fixture
def prepare_missing_config_file():
    file_input = {
        'template_file': 'tests/resources/sample_template.jinja2',
        'config_file': 'tests/resources/missing_config.yml'
    }

    return file_input


def _invoke_validator(template_file, config_file):
    abs_template_file = os.path.abspath(template_file)
    abs_config_file = os.path.abspath(config_file)

    validator_obj = VariableValidator(abs_template_file, abs_config_file)
    return validator_obj.validate()


def test_variable_validator(prepare_input):
    assert _invoke_validator(prepare_input['template_file'], prepare_input['config_file'])


def test_missing_variable(prepare_wrong_input):
    assert _invoke_validator(prepare_wrong_input['template_file'], prepare_wrong_input['config_file']) == False

def test_missing_template_file(prepare_missing_template_file):
    with pytest.raises(Exception) as ex:
        _invoke_validator(prepare_missing_template_file['template_file'], prepare_missing_template_file['config_file'])
    
    assert type(ex.value) is jinja2.exceptions.TemplateNotFound

def test_missing_config_file(prepare_missing_config_file):
    with pytest.raises(Exception) as ex:
        _invoke_validator(prepare_missing_config_file['template_file'], prepare_missing_config_file['config_file'])

    assert type(ex.value) is FileNotFoundError
