from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from Compressor import compressor
import timeit

app = Flask(__name__, static_folder=join(dirname(realpath(__file__)), 'static/'))

# MEMBUAT DIR KALAU BELUM ADA
ORIGINAL_FOLDER = join(dirname(realpath(__file__)), 'static/original/')
os.makedirs(ORIGINAL_FOLDER, exist_ok=True)
COMPRESSED_FOLDER = join(dirname(realpath(__file__)), 'static/compressed/')
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

app.secret_key = "pencitraan"
app.config['ORIGINAL_FOLDER'] = ORIGINAL_FOLDER
app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER
app.config['PREFIX_COMP'] = "compressed_"
app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def process_image():
    # GET REQUEST FILE DAN COMPRESSION RATE
    file = request.files['file']
    comprate = request.form.get('comp-rate', type=float)
    if (comprate%1==0):
        comprate = int(comprate)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['ORIGINAL_FOLDER'], filename))

        # MASUKKAN COMPRESSOR SVD DISINI
        start = timeit.default_timer()
        compressor(app.config['ORIGINAL_FOLDER'], app.config['COMPRESSED_FOLDER'], filename, comprate, app.config['PREFIX_COMP'])
        stop = timeit.default_timer()
        runtime = round(stop-start, 4)
        original_size = os.path.getsize(app.config['ORIGINAL_FOLDER'] + filename)
        compressed_size = os.path.getsize(app.config['COMPRESSED_FOLDER'] + app.config['PREFIX_COMP'] + filename)
        ratio_size = round((100*compressed_size)/original_size, 2)

        return render_template('home.html', filename=filename, cprate=ratio_size, runtime=runtime)
    else:
        flash('Allowed image types are: .png, .jpg, .jpeg, .gif')
        return redirect(request.url)

@app.route('/original/<filename>')
def display_org(filename):
    return redirect(url_for('static', filename='original/' + filename), code=301)

@app.route('/compressed/<filename>')
def display_comp(filename):
    return redirect(url_for('static', filename='compressed/' + app.config['PREFIX_COMP']+ filename), code=301)

@app.route('/how-to-use')
def howtouse():
    return render_template("howtouse.html")

@app.route('/about-us')
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)
