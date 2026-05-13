# TDD

## Repositório Git

https://github.com/joycesilvaaa/tdd.git

## Tecnologias

- Python 3.12
- pytest
- pytest-cov para cobertura de testes

## Estrutura do Projeto

- `triangle.py` - Lógica do exercício 1 (classificação de triângulos)
- `person.py` - Classes `Person`, `Email` e `PersonDAO` para o exercício 2
- `salary.py` - Cálculo de salário para o exercício 3
- `tests/` - Testes unitários
- `requirements.txt` - Dependências de teste

## Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/joycesilvaaa/tdd.git
cd tdd
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução de Testes

Para executar todos os testes:

```bash
python3 -m pytest
```

## Cobertura de Testes

Para gerar o relatório de cobertura:

```bash
python3 -m pytest --cov=. --cov-report=html
```

O relatório HTML estará disponível em `htmlcov/index.html`.

## Evidências de Cobertura por Exercício

| Exercício | Arquivo       | Cobertura |
|-----------|---------------|-----------|
| 1         | `triangle.py` | 100%     |
| 2         | `person.py`   | 100%     |
| 3         | `salary.py`   | 100%     |

## Exercícios Implementados

### Exercício 1 - Triângulo

**Arquivo:** `triangle.py`  
**Testes:** `tests/test_triangle.py`

Implementa a classificação de triângulos baseada em três lados inteiros. Valida se os lados formam um triângulo e classifica como equilátero, isósceles ou escaleno.

**Casos de teste cobertos:**
- Triângulo escaleno válido
- Triângulo isósceles válido (3 permutações)
- Triângulo equilátero válido
- Valores zero
- Valores negativos
- Soma de dois lados igual ao terceiro (3 permutações)
- Soma de dois lados menor que o terceiro (3 permutações)
- Todos os três valores iguais a zero

### Exercício 2 - Validação de Person

**Arquivos:** `person.py`  
**Testes:** `tests/test_person.py`

Implementa validação de objetos `Person` com regras específicas para nome, idade e emails.

**Validações realizadas:**
- Nome: pelo menos duas partes, contendo apenas letras
- Idade: intervalo [1, 200]
- Emails: pelo menos um associado, formato `local@dominio.tld`

### Exercício 3 - Cálculo de Salário

**Arquivo:** `salary.py`  
**Testes:** `tests/test_salary.py`

Calcula o salário líquido de funcionários baseado no cargo e salário base.

**Regras implementadas:**
- **Desenvolvedor:** 20% de desconto se salário >= 3.000,00; 10% caso contrário
- **DBA:** 25% de desconto se salário >= 2.000,00; 15% caso contrário
- **Testador:** 25% de desconto se salário >= 2.000,00; 15% caso contrário
- **Gerente:** 30% de desconto se salário >= 5.000,00; 20% caso contrário
