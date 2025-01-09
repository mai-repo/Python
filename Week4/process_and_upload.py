import os
import requests # This is a third party library that you need to install to request HTTP requests
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def process_file(file_path):
    with open (file_path, 'r') as file:
        data = file.read()

        #process that data and return a dictionary 
        feedback_dic = json.loads(data)
        return feedback_dic

if __name__= "__main__":
    app.run(debug=True, port=5000) # Run the app in debug mode and on port 5000

    