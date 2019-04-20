from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> abcd </h1>"

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    BMI = weight/((height/100)**2)
    # return render_template("BMI.html",BMI = BMI)    #day la cach dung render
    result = 0 
    if BMI < 16:
        result = "severely underweight"
    elif BMI < 18.5:
        result = "underweight"
    elif BMI < 25:
        result = "normal"
    elif BMI < 30:
        result = "overweight"
    else:
        result = "obese"
    return result

if __name__ == '__main__':
  app.run(debug=True)
 