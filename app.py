from flask import Flask
from services.age_pipeline import process_age_time
from services.overview_pipeline import process_overview_alliance
# from pathlib import Path

app = Flask(__name__)

URL = "https://www.webgame.cz/"

@app.route("/")
def homepage():
    present_age = process_age_time(URL)
    data = { "name" : present_age.data.name,
             "start": present_age.data.start,
             "end": present_age.data.end,
             "rest": present_age.data.rest_time,
             "error": present_age.errors,
    }
    errors = present_age.errors  
    return data



# def initiate_function():
#     return "The server live and initiate new page"
    

# DATA_URL = Path(__file__).parents[1] / "tests" / "fixtures" / "overview_parser_test_data" / "original_NTRLTY_aliance.html"

# html = DATA_URL.read_text(encoding="utf-8")
    
    
if __name__ == '__main__':
    app.run(debug=True)