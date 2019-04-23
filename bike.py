from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
  return "Hello"

bike_list = []

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
    bike_list.append(new_list)
    return redirect("/your_bike")

@app.route("/your_bike")
def your_bike():
  return render_template("your_bike.html", bike_list = bike_list)

if __name__ == '__main__':
  app.run(debug=True)
 