from flask import Flask
from services.age_pipeline import process_age_time

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
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)