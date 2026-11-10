# tempconv

A small Python command-line tool that converts temperatures between Celsius, Fahrenheit and Kelvin.

## Install

```bash
pip install -r requirements-dev.txt
```

## Usage

```bash
python -m tempconv 100 --from C --to F    # 100 C = 212 F
python -m tempconv 300 --from K --to C    # 300 K = 26.85 C
python -m tempconv -500 --from C --to K   # error: below absolute zero (exit code 2)
```

Supported units: `C` (Celsius), `F` (Fahrenheit), `K` (Kelvin).

Temperatures below absolute zero (-273.15 C = -459.67 F = 0 K) are rejected: the library raises
`BelowAbsoluteZeroError` (a `ValueError`) and the CLI prints an error and exits with code 2.

As a library:

```python
from tempconv.core import convert
convert(100, "C", "F")   # 212.0
```

## Tests

```bash
pytest
```

The tests cover known C/F/K conversions, round trips, the absolute-zero check for every unit and the CLI.

## License

MIT
