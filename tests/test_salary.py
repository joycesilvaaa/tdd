import pytest
from decimal import Decimal

from salary import Employee, Role, SalaryCalculator


def test_developer_above_threshold():
    employee = Employee("Dev", "dev@empresa.com", Decimal("3000.00"), Role.DESENVOLVEDOR)
    assert SalaryCalculator.calculate_net(employee) == Decimal("2400.00")


def test_developer_below_threshold():
    employee = Employee("Dev", "dev@empresa.com", Decimal("2999.99"), Role.DESENVOLVEDOR)
    assert SalaryCalculator.calculate_net(employee) == Decimal("2699.99")


def test_dba_above_threshold():
    employee = Employee("Dba", "dba@empresa.com", Decimal("2000.00"), Role.DBA)
    assert SalaryCalculator.calculate_net(employee) == Decimal("1500.00")


def test_dba_below_threshold():
    employee = Employee("Dba", "dba@empresa.com", Decimal("1999.99"), Role.DBA)
    assert SalaryCalculator.calculate_net(employee) == Decimal("1699.99")


def test_tester_above_threshold():
    employee = Employee("Tester", "tester@empresa.com", Decimal("2000.00"), Role.TESTADOR)
    assert SalaryCalculator.calculate_net(employee) == Decimal("1500.00")


def test_manager_above_threshold():
    employee = Employee("Manager", "manager@empresa.com", Decimal("5000.00"), Role.GERENTE)
    assert SalaryCalculator.calculate_net(employee) == Decimal("3500.00")


def test_manager_below_threshold():
    employee = Employee("Manager", "manager@empresa.com", Decimal("4999.99"), Role.GERENTE)
    assert SalaryCalculator.calculate_net(employee) == Decimal("3999.99")


def test_unknown_role_raises_error():
    employee = Employee("Unknown", "unknown@empresa.com", Decimal("1000.00"), "INVALID")

    with pytest.raises(ValueError, match="Cargo desconhecido"):
        SalaryCalculator.calculate_net(employee)
