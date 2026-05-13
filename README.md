## Repositório Git

https://github.com/joycesilvaaa/tdd.git

## Tecnologias

- Python 3.12
- pytest
- pytest-cov para cobertura de testes

## Estrutura do projeto

- `triangle.py` - lógica do exercício 1
- `person.py` - classes `Person`, `Email` e `PersonDAO` para o exercício 2
- `salary.py` - cálculo de salário para o exercício 3
- `tests/` - testes unitários
- `requirements.txt` - dependências de teste

## Como preparar o ambiente

1. Instale as dependências do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como executar os testes

```bash
python3 -m pytest
```

## Como gerar cobertura de testes

```bash
python3 -m pytest --cov=. --cov-report=html
```

Após a execução, o relatório de cobertura estará disponível em `htmlcov/index.html`.

## Evidências de cobertura por exercício

- Exercício 1 (`triangle.py`): cobertura de 100%
- Exercício 2 (`person.py`): cobertura de 100% (inclui `PersonDAO.save` e validações de nome, idade e email)
- Exercício 3 (`salary.py`): cobertura de 100%

Os relatórios detalhados de cobertura estão disponíveis em `htmlcov/index.html`.

## Exercícios implementados

### Exercício 1 - Triângulo

- Classe/funcionalidade em `triangle.py`
- Testes em `tests/test_triangle.py`
- Casos cobertos:
  - Triângulo escaleno válido
  - Triângulo isósceles válido
  - Triângulo equilátero válido
  - 3 permutações de isósceles válido
  - Um valor zero
  - Um valor negativo
  - Soma de dois lados igual ao terceiro (3 permutações)
  - Soma de dois lados menor que o terceiro (3 permutações)
  - Todos os três valores iguais a zero

### Exercício 2 - Validação de Person

- Classes em `person.py`
- Testes em `tests/test_person.py`
- Validações realizadas:
  - nome com pelo menos duas partes e apenas letras
  - idade no intervalo [1, 200]
  - pelo menos um email associado
  - formato de email `local@dominio.tld`

### Exercício 3 - Cálculo de salário

- Classes em `salary.py`
- Testes em `tests/test_salary.py`
- Regras implementadas:
  - Desenvolvedor: 20% de desconto para salário >= 3.000,00 e 10% caso contrário
  - DBA: 25% de desconto para salário >= 2.000,00 e 15% caso contrário
  - Testador: 25% de desconto para salário >= 2.000,00 e 15% caso contrário
  - Gerente: 30% de desconto para salário >= 5.000,00 e 20% caso contrário
