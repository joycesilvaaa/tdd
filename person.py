import re
from dataclasses import dataclass, field
from typing import List

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$")

@dataclass
class Email:
    id: int
    name: str


@dataclass
class Person:
    id: int
    name: str
    age: int
    emails: List[Email] = field(default_factory=list)


class PersonDAO:
    _store: List[Person] = []

    @classmethod
    def save(cls, person: Person) -> None:
        errors = cls.is_valid_to_include(person)
        if errors:
            raise ValueError("Pessoa inválida: " + "; ".join(errors))
        cls._store.append(person)

    @classmethod
    def list_all(cls) -> List[Person]:
        return list(cls._store)

    @classmethod
    def clear_store(cls) -> None:
        cls._store.clear()

    @staticmethod
    def is_valid_to_include(person: Person) -> List[str]:
        errors: List[str] = []

        if person is None:
            errors.append("Pessoa não pode ser nula")
            return errors

        PersonDAO._validate_name(person.name, errors)
        PersonDAO._validate_age(person.age, errors)
        PersonDAO._validate_emails(person.emails, errors)

        return errors

    @staticmethod
    def _validate_name(name: str, errors: List[str]) -> None:
        if name is None or not name.strip():
            errors.append("Nome deve ser composto por ao menos 2 partes e conter apenas letras")
            return

        parts = name.strip().split()
        if len(parts) < 2:
            errors.append("Nome deve ser composto por ao menos 2 partes e conter apenas letras")
            return

        for part in parts:
            if not part.isalpha():
                errors.append("Nome deve ser composto por ao menos 2 partes e conter apenas letras")
                return

    @staticmethod
    def _validate_age(age: int, errors: List[str]) -> None:
        if age < 1 or age > 200:
            errors.append("Idade deve estar no intervalo [1, 200]")

    @staticmethod
    def _validate_emails(emails: List[Email], errors: List[str]) -> None:
        if not emails:
            errors.append("Pessoa deve ter pelo menos um email associado")
            return

        for email in emails:
            if email is None or email.name is None or not email.name.strip():
                errors.append("Email deve estar no formato local@dominio.tld")
                continue
            if not PersonDAO._is_valid_email(email.name):
                errors.append("Email deve estar no formato local@dominio.tld")

    @staticmethod
    def _is_valid_email(value: str) -> bool:
        if not EMAIL_PATTERN.match(value):
            return False

        local, domain = value.split("@", 1)
        domain_parts = domain.split(".")
        return len(domain_parts) >= 2 and all(part for part in domain_parts)
