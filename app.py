from flask import Flask
from parsers.age import parse_age

app = Flask(__name__)

@app.route("/")
def homepage():
    present_age = parse_age
    return present_age
    

# def initiate_function():
#     return "The server live and initiate new page"
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)