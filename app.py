from flask import Flask,render_template

app = Flask(__name__)

todos =[
    {"srno.":1,"title":"Task 1","desc":"Watch a movie.","date_created":"08-08-26","status":"Searching"}
 ]

@app.route("/")
def home():
    return render_template("index.html",alltodos=todos)

if __name__ == "__main__":
    app.run(debug=True)