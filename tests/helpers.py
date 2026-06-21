import json

from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" # fixtures folder

def load_fixture(filename: str) -> str:
    html_test_file = FIXTURE_DIR / filename
    return html_test_file.read_text(encoding="utf-8")

def load_fixture_just_path(filename: str) -> str:
    return Path(FIXTURE_DIR / filename)

def load_json_fixture(filename: str) -> dict:
    file_text = load_fixture(filename=filename)
    return json.loads(file_text)

def load_fixture_file_test(filename: str) -> str:
    path = FIXTURE_DIR / filename
    
    print()
    print("FIXTURE_DIR:", FIXTURE_DIR)
    print("filename:", filename)
    print("final path:", path)
    print("resolved:", path.resolve())
    print("parent exists:", path.parent.exists())
    print("file exists:", path.exists())

    if path.parent.exists():
        print("files in parent:")
        for item in path.parent.iterdir():
            print(" -", repr(item.name))

    return path.read_text(encoding="utf-8")
