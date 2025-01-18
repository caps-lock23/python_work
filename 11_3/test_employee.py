import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee("Gerard", 'Cada', 1_000_000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 1_005_000

def test_give_custom_raise(employee):
    employee.give_raise(500_000)
    assert employee.annual_salary == 1_500_000