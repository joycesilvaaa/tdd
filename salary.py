from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum


class Role(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


@dataclass
class Employee:
    name: str
    email: str
    base_salary: Decimal
    role: Role


class SalaryCalculator:
    @staticmethod
    def calculate_net(employee: Employee) -> Decimal:
        salary = employee.base_salary
        rate = SalaryCalculator._discount_rate(employee.role, salary)
        net = salary - (salary * rate)
        return net.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @staticmethod
    def _discount_rate(role: Role, salary: Decimal) -> Decimal:
        if role == Role.DESENVOLVEDOR:
            return Decimal("0.20") if salary >= Decimal("3000") else Decimal("0.10")
        if role in (Role.DBA, Role.TESTADOR):
            return Decimal("0.25") if salary >= Decimal("2000") else Decimal("0.15")
        if role == Role.GERENTE:
            return Decimal("0.30") if salary >= Decimal("5000") else Decimal("0.20")
        raise ValueError(f"Cargo desconhecido: {role}")
