from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/how-to-use')
def howtouse():
    return render_template("howtouse.html")

@app.route('/about-us')
def aboutus():
    return render_template("aboutus.html")
    
if __name__ == "__main__":
    app.run(debug=True)
