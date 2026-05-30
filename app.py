from flask import Flask

app = Flask(__name__)

@app.route("/")
def initiate_function():
    return "The server live and initiate new page"
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)