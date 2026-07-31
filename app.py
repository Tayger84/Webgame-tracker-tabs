from flask import Flask, render_template, request, redirect
from data_services.age_pipeline import process_age_time
from data_services.main_pipeline import load_main_pipeline
from data_output.tabs_pipeline import get_data_for_processing

app = Flask(__name__)

URL = "https://www.webgame.cz/"

@app.route("/")
def home():

    return render_template(
        'base.html',
    )

@app.route("/upload", methods=["GET", "POST"])
def upload():
        
    if request.method == "POST":
        overview_file = request.files.get("overview_file")
        snapshot_file = request.files.get("snapshot_file")
        
        if not overview_file:
            return render_template(
                "upload.html",
                erorrs=["No overview HTTML file was uploaded"],
            )
            
        if not snapshot_file:
            return render_template(
                "upload.html",
                erorrs=["No overview HTML file was uploaded"],
            )
    
        overview_html = overview_file.read().decode("utf-8", errors="replace")
        snapshot_html = snapshot_file.read().decode("utf-8", errors="replace")
        

        load_result = load_main_pipeline(overview_html, snapshot_html)
        alliance_data = load_result.countries_final_data
        
        get_data_for_processing(alliance_data)

        return render_template(
                    "result.html",
                    errors=[],
                    alliance_data=alliance_data,
                )    

    
    return render_template(
        'upload.html',
        errors=[],
    )

if __name__ == '__main__':
    app.run(debug=True)