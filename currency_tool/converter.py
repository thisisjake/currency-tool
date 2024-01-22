from typing import List
from decimal import Decimal

from currency_tool._currency_table_builder import _CurrencyTableBuilder


class CurrencyConverter:
    def __init__(self, currencies: List):
        self._currency_tables = _CurrencyTableBuilder._build(currencies)
    
    def convert(self, amount: Decimal, currency_in: str, currency_out: str, date: str):
        conversion_rate = self._currency_tables[currency_in + '_' + currency_out].get(date)

        if not conversion_rate:
            # TODO Download via API
            converted_amount = 'retrieved value'            # FIX THIS

        converted_amount = conversion_rate * amount
        
        if currency_out == 'JPY':
            return converted_amount.quantize(Decimal('0'))
        
        return converted_amount.quantize(Decimal('0.00'))
