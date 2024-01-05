import os

from flask import Flask, render_template, request, jsonify
from flask_dropzone import Dropzone
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'static/uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000,
    DROPZONE_UPLOAD_ON_CLICK=True
    )

dropzone = Dropzone(app)
@app.route('/',methods=['POST','GET'])
def upload():
    count = 0
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
                count += 1
        if count == 1:
            return render_template('index.html')
        elif count > 1:
            return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)