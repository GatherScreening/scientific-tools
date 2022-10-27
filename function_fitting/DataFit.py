from flask import Flask, redirect, url_for, request, render_template,Blueprint
from werkzeug.utils import secure_filename
import os

"""
数据预测接口
"""

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'

datafit = Blueprint('datafit', __name__, template_folder='templates')
# 接收文件，可以上传压缩包或者多个文件(.csv)
@datafit.route("/data/predict", methods=['POST'])
def data_predict():
    file = request.files.getlist('key')
    print(file)
    for f in file:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return "success"







