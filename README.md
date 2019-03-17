# is-natural-number

> Check if a value is a [natural number](https://en.wikipedia.org/wiki/Natural_number).

I'm aspiring to make open-source my full-time work. If you or your company likes the work that I do, please consider supporting me.

[![Coffee][badge_coffee_donate]](https://www.buymeacoffee.com/adamzerella)
[![PayPal][badge_paypal_donate]](https://www.paypal.me/adamzerella)

## Install

```bash
pip install is_natural_number
```

## Usage
```python
from is_natural_number import isNaturalNumber

isNaturalNumber(5)            // True
isNaturalNumber(0)            // False
isNaturalNumber(0, True)      // True
isNaturalNumber(-5)           // False
isNaturalNumber('-45')        // False
```

## API

### isNaturalNumber(value, includeZero)

value: `int, str` - Value to check

includeZero: `bool` - Whether or not to consider `0` as a natural number.

## Test

```bash
python test.py
```

## Contribute

Don't be scared raise an issue or a pull request! Any contributions, no matter how big or small will land your picture here.

<div style="display:inline;">
  <a href="https://github.com/adamzerella"><img width="64" height="64" src="https://avatars0.githubusercontent.com/u/1501560?s=460&v=4" alt="Adam Zerella"/></a>
</div>

[badge_coffee_donate]: https://adamzerella.com/badges/coffee.svg
[badge_paypal_donate]: https://adamzerella.com/badges/paypal.svg