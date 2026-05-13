import pytest

from person import Email, Person, PersonDAO


def test_valid_person_is_accepted():
    person = Person(1, "Joao Silva", 30, [Email(1, "joao@empresa.com")])
    assert PersonDAO.is_valid_to_include(person) == []


def test_person_none_is_rejected():
    assert PersonDAO.is_valid_to_include(None) == ["Pessoa não pode ser nula"]


def test_person_with_empty_name_is_rejected():
    person = Person(1, "", 30, [Email(1, "joao@empresa.com")])
    assert "Nome deve ser composto por ao menos 2 partes e conter apenas letras" in PersonDAO.is_valid_to_include(person)


def test_blank_email_is_rejected():
    person = Person(1, "Maria Souza", 25, [Email(1, "")])
    assert "Email deve estar no formato local@dominio.tld" in PersonDAO.is_valid_to_include(person)


def test_save_valid_person_stores_person():
    PersonDAO.clear_store()
    person = Person(1, "Joao Silva", 30, [Email(1, "joao@empresa.com")])

    PersonDAO.save(person)

    assert PersonDAO.list_all() == [person]


def test_save_invalid_person_raises_error():
    PersonDAO.clear_store()
    person = Person(1, "Joao", 30, [Email(1, "joao@empresa.com")])

    with pytest.raises(ValueError, match="Pessoa inválida"):
        PersonDAO.save(person)


def test_name_with_single_part_is_rejected():
    person = Person(1, "Joao", 30, [Email(1, "joao@empresa.com")])
    assert "Nome deve ser composto por ao menos 2 partes e conter apenas letras" in PersonDAO.is_valid_to_include(person)


def test_name_with_non_letter_is_rejected():
    person = Person(1, "Joao 123", 30, [Email(1, "joao@empresa.com")])
    assert "Nome deve ser composto por ao menos 2 partes e conter apenas letras" in PersonDAO.is_valid_to_include(person)


def test_age_below_range_is_rejected():
    person = Person(1, "Joao Silva", 0, [Email(1, "joao@empresa.com")])
    assert "Idade deve estar no intervalo [1, 200]" in PersonDAO.is_valid_to_include(person)


def test_age_above_range_is_rejected():
    person = Person(1, "Joao Silva", 201, [Email(1, "joao@empresa.com")])
    assert "Idade deve estar no intervalo [1, 200]" in PersonDAO.is_valid_to_include(person)


def test_person_without_email_is_rejected():
    person = Person(1, "Maria Souza", 25, [])
    assert "Pessoa deve ter pelo menos um email associado" in PersonDAO.is_valid_to_include(person)


def test_invalid_email_format_is_rejected():
    person = Person(1, "Maria Souza", 25, [Email(1, "maria@empresa")])
    assert "Email deve estar no formato local@dominio.tld" in PersonDAO.is_valid_to_include(person)
