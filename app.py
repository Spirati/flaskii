from flask import Flask, request, redirect, flash, render_template
from image import validate, processImage
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()

    app = Flask(import_name=__name__)
    app.secret_key = os.getenv("FLASK_KEY", None)

    if app.secret_key is None:
        raise RuntimeError("Secret key was not set!")

    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route("/process", methods=["GET", "POST"])
    def process():
        if request.method == "POST":
            im = validate(request.files.get("img", None))
            if im is None:
                flash("ARGH")
                return redirect("/")
            
            final = processImage(im)

            return render_template("processed.html", image=final)
            
            

    return app