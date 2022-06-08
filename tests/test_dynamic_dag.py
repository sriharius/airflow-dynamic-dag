

import pytest
from dynamic_dag import DynamicDagFactory, SingleDynamicDagCreator, MultipleDynamicDagCreator


@pytest.fixture
def prepare_single_input():
    args = {
        'cmd': 'single'
    }

    return args

@pytest.fixture
def prepare_multiple_input():
    args = {
        'cmd': 'multiple'
    }

    return args

def test_factory_single(prepare_single_input):
    obj = DynamicDagFactory.get_dag_creator(prepare_single_input)
    assert type(obj) is SingleDynamicDagCreator

def test_factory_multiple(prepare_multiple_input):
    obj = DynamicDagFactory.get_dag_creator(prepare_multiple_input)
    assert type(obj) is MultipleDynamicDagCreator
