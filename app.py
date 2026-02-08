import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Photo save karne ki jagah set karna
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max size

# Folder automatic bana dega agar nahi hai toh
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/valentine', methods=['POST'])
def preview():
    sender = request.form.get('sender', 'Secret Admirer')
    recipient = request.form.get('recipient', 'My Valentine')
    template = request.form.get('template', 'playful')
    message = request.form.get('message', "I have a question for you...")
    
    photo_filename = None
    if 'photo' in request.files:
        file = request.files['photo']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_filename = filename

    return render_template('preview.html', 
                           sender=sender, 
                           recipient=recipient, 
                           template=template, 
                           message=message,
                           photo=photo_filename)

if __name__ == '__main__':
    app.run(debug=True)