from flask import Flask, render_template, request
import requests
# from app import app
from forms import SearchForm
from config import Config

app = Flask("app")
app.config.from_object(Config)

# Routes
@app.route("/", methods=["GET"])
def index():
  # return "hi"
  return render_template("index.html.j2")

@app.route("/search", methods=["GET", "POST"])
def search():
  form = SearchForm()
  if request.method == "POST" and form.validate_on_submit():
    p_name = form.name.data.lower()
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{p_name}")
    # See if pokemon exists
    if res:
      poke_json = res.json()
      poke_json["name"] = poke_json["name"].title()
      return render_template("poke_info.html.j2", poke=poke_json)
    error_string = "Can't find Pokemon!"
    return render_template("search.html.j2", error=error_string, form=form)

  return render_template("search.html.j2", form=form)

@app.route("/poke_info", methods=["GET"])
def poke_info():
  pass