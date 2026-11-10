"""Temperature conversions between Celsius, Fahrenheit and Kelvin."""

ABSOLUTE_ZERO_C = -273.15


class BelowAbsoluteZeroError(ValueError):
    """Raised when a temperature is colder than absolute zero."""


def _check_celsius(c: float) -> float:
    if c < ABSOLUTE_ZERO_C:
        raise BelowAbsoluteZeroError(f"{c} C is below absolute zero ({ABSOLUTE_ZERO_C} C)")
    return c


def to_celsius(value: float, unit: str) -> float:
    unit = unit.upper()
    if unit == "C":
        c = value
    elif unit == "F":
        c = (value - 32) * 5 / 9
    elif unit == "K":
        c = value + ABSOLUTE_ZERO_C
    else:
        raise ValueError(f"Unknown unit: {unit} (use C, F or K)")
    return _check_celsius(c)


def from_celsius(c: float, unit: str) -> float:
    _check_celsius(c)
    unit = unit.upper()
    if unit == "C":
        return c
    if unit == "F":
        return c * 9 / 5 + 32
    if unit == "K":
        return c - ABSOLUTE_ZERO_C
    raise ValueError(f"Unknown unit: {unit} (use C, F or K)")


def convert(value: float, src: str, dst: str) -> float:
    """Convert value from unit src to unit dst (C, F or K)."""
    return round(from_celsius(to_celsius(value, src), dst), 2)
