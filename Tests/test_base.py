import pytest
from congtest import init_driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
