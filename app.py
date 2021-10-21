from flask import Flask

UPLOAD_FOLDER = 'C:/Users/lakis/OneDrive/Desktop'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 # 50MB