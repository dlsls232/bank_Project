# Bank Project

Проект для работы с банковскими транзакциями.

## Генераторы (`src/generators.py`)

Модуль содержит три генератора:

* `filter_by_currency(transactions, currency)` — возвращает транзакции в указанной валюте.
* `transaction_descriptions(transactions)` — возвращает описания транзакций.
* `card_number_generator(start, end)` — генерирует номера карт в формате `XXXX XXXX XXXX XXXX`.

### Примеры использования

```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 3):
    print(card_number)
```

Результат:

```text
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
```

## Тестирование

Запуск тестов:

```bash
poetry run pytest
```

Проверка покрытия кода:

```bash
poetry run pytest --cov=src.generators --cov-report=term-missing --cov-report=html tests
```

HTML-отчёт о покрытии создаётся в папке `htmlcov`.

Тесты генераторов проверяют фильтрацию транзакций по валюте, получение описаний и генерацию номеров карт.
