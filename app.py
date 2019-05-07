from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
from food_db import Foods, Users
from bson.objectid import ObjectId

app.config["SECRET_KEY"] = "fasd12daf238gfh8hf1$%182###"

@app.route('/')             #dau / khong co gi dang sau la trang chu
def index():
    return "C4E29 hello"  

@app.route("/say-hi")
def say_hi():
    return "hi everyone"

@app.route("/say-hi/<name>")
def say_hi_everyone(name):
    return "xin chao {}".format(name)

@app.route("/add/<int:x>/<int:y>")
def sum_total(x,y):
    total = x + y
    return str(total)

@app.route("/food")
def food():
    if "logged" in session:
        if session["logged"] == True:
            food_list = Foods.find()
            return render_template("food.html",food_list = food_list)            #co the viet html code vao return
        else: 
            return redirect("/login")
    else:
        return redirect ("/login")
@app.route("/food/<id>")
def detail(id):
    detail_food = Foods.find_one({"_id": ObjectId(id)})
    return render_template("food_detail.html", detail_food = detail_food)

@app.route("/food/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("add_food.html")
    elif request.method == "POST":
        form = request.form
        new_food = {
            "title": form["title"],
            "description": form["description"],
            "link": form["link"],
            "type": form["type"],
        }
        Foods.insert_one(new_food)
        return redirect("/food")

@app.route("/food/edit/<id>", methods = ["GET","POST"])
def edit_food(id):
    food = Foods.find_one({"_id": ObjectId(id)}) 
    if request.method == "GET":
        return render_template("edit_food.html", food = food) 
    elif request.method == "POST":
        form = request.form
        new_value = { "$set": {
            "title": form["title"],
            "description": form["description"],
            "link": form["link"],
            "type": form["type"],
        } }
        Foods.update_one(food,new_value)
        return redirect("/food")

@app.route("/food/delete/<id>")
def delete_food(id):
    food = Foods.find_one({ "_id": ObjectId(id) })
    Foods.delete_one(food)
    return redirect("/food")

# info = {
#     "name" : "C4E",
#     "password": "C4E",
# }

@app.route("/login", methods = ["GET", "POST"])
def login():
    if "logged" in session:
        if session["logged"] == True:
            return redirect("/food")
        else:
            if request.method == "GET":
                return render_template("login.html")
            if request.method == "POST":
                form = request.form 
                login_username = form["name"]
                login_password = form["password"]
                user = Users.find_one({"username":login_username})
                if user is None:
                    session["logged"] = False
                    return redirect("/login")
                else:   
                    if login_password == user["password"]:
                        session["logged"] = True
                        return redirect("/food")
                    else:
                        session["logged"] = False
                        return redirect("/login")
    else:
        session["logged"] = False
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "logged" in session:
        session["logged"] = False 
    return redirect("/login")
        
@app.route("/register", methods = ["GET", "POST"]) 
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        register_username = form["register_username"]
        register_password = form["register_password"]
        new_user = {
            "username": register_username,
            "password": register_password,
        }
        Users.insert_one(new_user)
        return redirect("/login")
    

if __name__ == '__main__':          #kiem tra xem file co dang chay truc tiep hay khong? chay gian tiep se la == "_test_"
  app.run(debug=True)
 