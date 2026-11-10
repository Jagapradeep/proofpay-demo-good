import pytest

from tempconv.__main__ import main
from tempconv.core import BelowAbsoluteZeroError, convert


@pytest.mark.parametrize("value,src,dst,expected", [
    (100, "C", "F", 212),
    (0, "C", "F", 32),
    (32, "F", "C", 0),
    (-40, "F", "C", -40),
    (0, "K", "C", -273.15),
    (25, "C", "K", 298.15),
    (212, "F", "K", 373.15),
    (373.15, "K", "F", 212),
])
def test_known_conversions(value, src, dst, expected):
    assert convert(value, src, dst) == pytest.approx(expected)


@pytest.mark.parametrize("value,unit,other", [(37.5, "C", "F"), (98.6, "F", "K"), (300, "K", "C")])
def test_round_trip(value, unit, other):
    assert convert(convert(value, unit, other), other, unit) == pytest.approx(value, abs=0.01)


@pytest.mark.parametrize("value,unit", [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_rejects_below_absolute_zero_for_each_unit(value, unit):
    with pytest.raises(BelowAbsoluteZeroError):
        convert(value, unit, "C" if unit != "C" else "F")


def test_absolute_zero_itself_is_allowed():
    assert convert(0, "K", "C") == pytest.approx(-273.15)


def test_cli_prints_result(capsys):
    assert main(["100", "--from", "C", "--to", "F"]) == 0
    assert "100 C = 212 F" in capsys.readouterr().out


def test_cli_error_exit_code(capsys):
    assert main(["-500", "--from", "C", "--to", "K"]) == 2
    assert "below absolute zero" in capsys.readouterr().err
