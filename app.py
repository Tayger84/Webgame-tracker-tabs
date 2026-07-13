from flask import Flask, render_template, request, redirect
from data_services.age_pipeline import process_age_time
from data_services.overview_pipeline import process_overview_alliance
from data_services.snapshot_pipeline import process_snapshot_alliance

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
        
        overview_result = process_overview_alliance(overview_html)
        snapshot_result = process_snapshot_alliance(snapshot_html)
        
        errors = []
        
        if not overview_result.ok:
            errors.append(overview_result.errors)
            
        if not snapshot_result.ok:
            errors.append(snapshot_result.errors)
            
        if errors:
            return render_template(
                "upload.html",
                errors=errors,
                overview_result=overview_result,
                snapshot_result=snapshot_result,
            ) 

        return render_template(
            "result.html",
            errors=[],
            overview_result=overview_result,
            snapshot_result=snapshot_result,
        )
    
    
    return render_template(
        'upload.html',
        errors=[],
    )

if __name__ == '__main__':
    app.run(debug=True)