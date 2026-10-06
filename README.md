# Bank Project

Проект учебного виджета банковских операций клиента. В проекте реализованы
функции маскировки номеров карт и счетов, форматирования даты, фильтрации
операций по состоянию и сортировки операций по дате.

## Установка

1. Клонируйте репозиторий:

```bash
git clone <URL-репозитория>
cd bank_Project
```

2. Создайте виртуальное окружение и установите зависимости проекта.

Если используется Poetry:

```bash
poetry install
```

## Использование

### Маскировка карты или счёта

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
```

### Форматирование даты

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
```

### Фильтрация операций

Функция `filter_by_state` по умолчанию оставляет операции со статусом
`EXECUTED`:

```python
from src.processing import filter_by_state

operations = [
    {"state": "EXECUTED", "id": 1},
    {"state": "CANCELED", "id": 2},
]

print(filter_by_state(operations))
print(filter_by_state(operations, "CANCELED"))
```

### Сортировка операций по дате

Функция `sort_by_date` по умолчанию сортирует операции от самой новой к
самой старой. Для сортировки от старой даты к новой передайте
`descending=False`:

```python
from src.processing import sort_by_date

operations = [
    {"date": "2024-03-11T02:26:18"},
    {"date": "2024-04-01T10:00:00"},
]

print(sort_by_date(operations))
print(sort_by_date(operations, descending=False))
```

## Проверка проекта

Запуск всех тестов:

```bash
pytest
```

Проверка покрытия тестами:

```bash
pytest --cov=src --cov-report=term-missing
```

Создание HTML-отчёта покрытия:

```bash
pytest --cov=src --cov-report=html:htmlcov
```

После выполнения команды HTML-отчёт находится в папке `htmlcov/`.

Проверка стиля и типов:

```bash
flake8 src tests
isort --check-only src tests
mypy src
```

## Структура проекта

```text
bank_Project/
├── src/
│   ├── __init__.py
│   ├── masks.py
│   ├── processing.py
│   └── widget.py
├── tests/
│   └── test_processing.py
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## GitFlow

Разработка ведётся в отдельных feature-ветках. Готовые изменения передаются
в ветку `develop` через Pull Request. Ветка `main` используется как основная
ветка проекта.
