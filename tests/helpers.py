import json

from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" # fixtures folder

def load_fixture(filename: str) -> str:
    html_test_file = FIXTURE_DIR / filename
    return html_test_file.read_text(encoding="utf-8")

def load_json_fixture(filename: str) -> dict:
    file_text = load_fixture(filename=filename)
    return json.loads(file_text)