
if __name__ == "__main__":
    TEST_DIR = Path(__file__).resolve().parents[1]
    file_dir = TEST_DIR / "test_files" / "NTRLTY_aliance.html"

    with file_dir.open("r", encoding="utf-8") as overview:
        
        html = overview.read()
        
    # parsed = load_alliance_overview_data(html)
    # print(parsed)

