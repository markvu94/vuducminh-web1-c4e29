from flask import Flask, render_template, redirect
app = Flask(__name__)

info = {
    "name": "Vu Duc Minh",
    "school": "techkid",
    "hobbies": "football",
    "age": 24,
    "link": "https://i2-prod.mirror.co.uk/incoming/article14430745.ece/ALTERNATES/s615/0_SSC-Napoli-v-Arsenal-UEFA-Europa-League-Quarter-Final-Second-Leg.jpg",
}

@app.route('/')
def index():
    return "hello"

@app.route("/about_me")
def about_me():
    return render_template("about_me.html", info = info)

@app.route("/school")
def school():
    return redirect("https://mindx.edu.vn/")

if __name__ == '__main__':
  app.run(debug=True)
 