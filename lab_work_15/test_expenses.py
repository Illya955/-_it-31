
from expenses import parse_line


def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")

    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["date"] == "2026-09-21"


def test_parse_line_comment():
    record = parse_line("2026-09-22;transport;50.00;taxi")

    assert record["comment"] == "taxi"


def test_parse_line_amount():
    record = parse_line("2026-09-23;food;120.00;dinner")

    assert record["amount"] == 120.0

import pytest


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-21;food;85.50;lunch", "food", 85.50),
        ("2026-09-22;transport;50.00;taxi", "transport", 50.00),
        ("2026-09-23;food;120.00;dinner", "food", 120.00),
        ("2026-09-24;shopping;250.00;clothes", "shopping", 250.00),
        ("2026-09-25;food;45.00;coffee", "food", 45.00),
    ]
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    record = parse_line(line)

    assert record["category"] == expected_category
    assert record["amount"] == expected_amount

from expenses import load_expenses, total_by_category

def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"

    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8",
    )

    records = load_expenses(path)
    totals = total_by_category(records)

    assert totals == {"food": 100.0}

def test_real_expenses_file():
    records = load_expenses("data/expenses.csv")
    totals = total_by_category(records)

    assert totals == {
        "food": 1150.0,
        "transport": 120.0,
        "coffee": 135.0,
        "books": 350.0,
        "internet": 250.0,
    }