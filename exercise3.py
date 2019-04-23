from flask import Flask, render_template
app = Flask(__name__)

Users = {
  "huy" : {
            "name": "huy",
            "age" : 24,
          },
  "minh": {
            "name": "minh",
            "age" : 26,
          },
}

@app.route('/')
def index():
    return "hello world"

@app.route("/user/<username>")
def user(username):
  if username in Users:
    user_name = Users[username]
    return render_template("username.html", user_name = user_name)
  else:
    return "user not found"

if __name__ == '__main__':
  app.run(debug=True)
 