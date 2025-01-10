import os
import requests # This is a third party library that you need to install to request HTTP requests
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def process_file(file_path):
    try:
        with open (file_path, 'r') as file:
            data = file.read() #process that data and return a dictionary 
            feedback_dic = json.loads(data)
            return feedback_dic
    except Exception as e:
        print(f"An error occured: {e}")
        return None 

def upload_to_web_service(data):
    try:
        response = requests.post("http://localhost:5000/feedback", json=data)
        return response.status_code
    except Exception as e:
        print(f"An error occured: {e}")
        return None

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(file.filename)
    data = process_file(file.filename)
    if data:
        status_code = upload_to_web_service(data)
        if status_code == 201:
            return jsonify({"message": "File uploaded successfully"}), 201
        else:
            return jsonify({"message": "An error occured while uploading the file"}), 500
    else:
        return jsonify({"message": "An error occured while processing the file"}), 500

if __name__= "__main__":
    app.run(debug=True, port=5000) # Run the app in debug mode and on port 5000

    