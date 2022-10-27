# -*- coding: utf-8 -*-
from flask import Flask
from function_fitting.DataFit import datafit

app = Flask(__name__)
app.register_blueprint(datafit)


if __name__ == '__main__':
    app.run()
