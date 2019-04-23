from flask import Flask, render_template, request, redirect
app = Flask(__name__)

food_list = [
        {
            "title": "thit cho",
            "description": "rat ngon",
            "link": "https://cdnmedia.baotintuc.vn/Upload/BUnOnh8kCJUksZiuSPj5yg/files/thit%20cho(1).jpg",
            "type": "eat"
        },
        {
            "title": "thit meo",
            "description": "rat chua",
            "link": "https://upload.wikimedia.org/wikipedia/vi/thumb/0/0c/Thitmeo.jpg/300px-Thitmeo.jpg",
            "type": "eat"
        },
        {
            "title": "thit chuot",
            "description": "rat thoi",
            "link": "http://www.xaluan.com/images/news/Image/2017/12/07/95a295c786fd73.img.jpg",
            "type": "eat"
        },
        {
            "title": "nuoc chanh",
            "description": "rat thom",
            "link": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Lemonade_%28Lime_version%29.jpg/300px-Lemonade_%28Lime_version%29.jpg",
            "type": "drink"
        },
        {
            "title": "nuoc cam",
            "description": "rat good",
            "link": "https://images.kienthuc.net.vn/Uploaded/dinhcuc/2018_03_24/sang/2_ULTZ.jpg",
            "type": "drink"
        },
        {
            "title": "nuoc dau",
            "description": "rat good",
            "link": "https://media.lamsao.com//Resources/Data/News/Auto/thuyptt/201405/58520854bf65b03bbfc36359f6781022635362634918264039.jpg",
            "type": "drink"
        },
    ]

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
    return render_template("food.html",food_list = food_list)            #co the viet html code vao return

@app.route("/food/<int:index>")
def detail(index):
    detail_food = food_list[index]
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
        food_list.append(new_food)
        return redirect("/food")

info = {
    "name" : "C4E",
    "password": "C4E",
}

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        form = request.form   
        loop = "sai cmnr"
        if form["name"] == info["name"] and form["password"] == info["password"]:
            loop = "welcome"
        return loop
        
@app.route("/register", methods = ["GET", "POST"]) 
def register():
    if request.method == "POST":
        form = request.form
        return "abc"
    

if __name__ == '__main__':          #kiem tra xem file co dang chay truc tiep hay khong? chay gian tiep se la == "_test_"
  app.run(debug=True)
 