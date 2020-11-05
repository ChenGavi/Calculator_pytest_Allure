# -*- coding=utf-8 -*-
import pytest

from src.Calculator import Calculator


@pytest.fixture(scope="session")
def build_object():
    print("Calculator initialize")
    return Calculator()
