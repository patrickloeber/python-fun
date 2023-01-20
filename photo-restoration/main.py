from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from photo_restorer import predict_image

UPLOAD_FOLDER = '/static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        full_filepath = "." + url_for('static', filename='images/' + filename)
        
        file.save(full_filepath)
        restored_img_url = predict_image(full_filepath)
        return render_template('index.html', filename=filename, restored_img_url=restored_img_url)
    else:
        return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)