from pathlib import Path
from unittest.mock import Mock

import pytest

from parsers.age_parser import load_age_time_data


FIXTURE_DIR = Path(__file__).parent


class FakeResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        return None


def mocked_get_from_fixture(filename):
    html = (FIXTURE_DIR / filename).read_text(encoding="utf-8")
    return Mock(return_value=FakeResponse(html))


def test_load_age_time_data_from_valid_page(monkeypatch):
    monkeypatch.setattr(
        "parsers.age_parser.requests.get",
        mocked_get_from_fixture("valid_age_page.html"),
    )

    result = load_age_time_data()

    assert result.ok is True
    assert result.errors == []
    assert result.data.name == "Age 97"
    assert result.data.start == "01.06.2026 18:00"
    assert result.data.end == "30.06.2026 18:00"
    assert result.data.rest_time == "17 dni 6 hodin"


def test_load_age_time_data_converts_empty_values_to_none(monkeypatch):
    monkeypatch.setattr(
        "parsers.age_parser.requests.get",
        mocked_get_from_fixture("empty_values_age_page.html"),
    )

    result = load_age_time_data()

    assert result.ok is True
    assert result.raw_values == [None, None, None, None]
    assert result.data.name is None
    assert result.data.start is None
    assert result.data.end is None
    assert result.data.rest_time is None


def test_load_age_time_data_returns_error_when_no_strong_tags(monkeypatch):
    monkeypatch.setattr(
        "parsers.age_parser.requests.get",
        mocked_get_from_fixture("no_time_data_page.html"),
    )

    result = load_age_time_data()

    assert result.ok is False
    assert result.errors == ["No time data found in the html"]


def test_load_age_time_data_currently_fails_when_theme_is_missing(monkeypatch):
    monkeypatch.setattr(
        "parsers.age_parser.requests.get",
        mocked_get_from_fixture("missing_theme_page.html"),
    )

    with pytest.raises(AttributeError):
        load_age_time_data()
