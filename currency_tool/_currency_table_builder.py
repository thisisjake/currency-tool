from typing import List, Dict
import csv
from decimal import Decimal, ROUND_HALF_UP


class _CurrencyTableBuilder:
    @staticmethod
    def _build(currency_pairs: List) -> Dict[str, Dict[str, Decimal]]:
        currency_tables = {}
        for currency_pair in currency_pairs:
            currency_tables[currency_pair] = {}
            with open('currency_rates/' + currency_pair + '.csv', 'r', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                for row in reader:
                    currency_tables[currency_pair][row[0]] = Decimal(row[1])
        return currency_tables