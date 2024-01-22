# Currency-Converter

### Import:
```from currency_tool.converter import converter```

### Define a list of currency_pairs to be used:

Create a list of the currency pairs to be loaded:

```currency_pairs = ['AUD_JPY', 'CAD_JPY', 'EUR_JPY', 'GBP_JPY', 'PLN_JPY', 'SEK_JPY', 'USD_JPY']```

### Initialise the class and pass the currencies:

Initialise: ```currency_converter = CurrencyConverter(currency_pairs)```

### Conversion Usage:

Access: ```print(currency_converter.convert(Decimal(100.00), 'AUD', 'JPY', '01/19/2024'))``` 

```Output: 9767```