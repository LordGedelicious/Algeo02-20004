from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__)

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/compressify/original/')

app.secret_key = "pencitraan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def upload_image():
    file = request.files['file']
    comprate = request.form.get('comp-rate', type=float)
    if (comprate%1==0):
        comprate = int(comprate)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('home.html', filename=filename, cprate=comprate)
    else:
        flash('Allowed image types are: .png, .jpg, .jpeg, .gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='compressify/original/' + filename), code=301)

@app.route('/how-to-use')
def howtouse():
    return render_template("howtouse.html")

@app.route('/about-us')
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)
