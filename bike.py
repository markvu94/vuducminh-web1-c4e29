from flask import Flask, render_template, request, redirect
from bike_db import bike_collection
app = Flask(__name__)


@app.route('/')
def index():
  return "Hello"



@app.route("/new_bike", methods = ["GET", "POST"])
def bike():
  if request.method == "GET":
    return render_template("new_bike.html")
  elif request.method == "POST":
    form = request.form
    new_list = {
      "model": form["model"],
      "fee": form["fee"],
      "Image": form["Image"],
      "Year": form["Year"],
    }
    bike_collection.insert_one(new_list)
    return redirect("/your_bike")

@app.route("/your_bike")
def your_bike():
  bike_list = bike_collection.find()
  return render_template("your_bike.html", bike_list = bike_list)

if __name__ == '__main__':
  app.run(debug=True)
 