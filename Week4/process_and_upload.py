import os
import requests # This is a third party library that you need to install to request HTTP requests
from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)
# Define the folder where files will be saved
UPLOAD_FOLDER = '/Users/thanhmai/Python_Assignments/Week4/data'

# Make sure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


file = '/Users/thanhmai/Python_Assignments/Week4/data/user_data.json'
spotify_file = '/Users/thanhmai/Python_Assignments/Week4/data/spotify_data.json'


def process_file(file_path): 
    try:
        with open (file_path, 'r') as file:
            data = file.read() #process that data and return a dictionary 
            feedback_dic = json.loads(data)
            return feedback_dic
    except Exception as e:
        print(f"An error occured: {e}")
        return None 
    
# This is the route that will be used to upload the file
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/file', methods=['GET'])
def get_feedback():
    try:
        file_data = process_file(file)
        if file_data:
            new_data = []
            for item in file_data:  # Loop through each dictionary in the list
                new_data.append({
                    "first_name": item["first_name"],
                    "email": item["email"]
                })
            return jsonify(new_data)
        else:
            return jsonify({"message": "Failed to process the file"}), 500
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"message": "An internal server error occurred"}), 500

@app.route('/spotify', methods=['GET'])
def get_spotify():
    try:
        spotify_data = process_file(spotify_file)
        new_spotify = []
        if spotify_data: 
            for spotify in spotify_data: 
                new_spotify.append({
                    "artist": spotify["artist"],
                    "vibe": spotify["vibe"]})
            return new_spotify
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"message": "An internal server error occurred"}), 500

# Route to handle file upload via POST request
# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' in request.files:
#         uploaded_file = request.files['file']
#         if uploaded_file.filename != '':
#             # Define the file path where it will be saved
#             file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
#             uploaded_file.save(file_path)

#             new_data_return = process_file(uploaded_file)
#             return jsonify(new_data_return)

#     return jsonify({"message": "No file provided or invalid file."}), 400

# Route to handle file upload via POST request
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400
    
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    try:
        # Define the file path where it will be saved
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(file_path)

        # Process the uploaded file (assuming it's a JSON file)
        new_data_return = process_file(file_path)
        
        # If file is processed correctly, return the data
        if new_data_return:
            return jsonify(new_data_return), 200
        else:
            return jsonify({"message": "Failed to process the file as valid JSON"}), 500
    except Exception as e:
        print(f"An error occurred during file upload: {e}")
        return jsonify({"message": "An error occurred while processing the uploaded file"}), 500

if __name__== "__main__":
    app.run(debug=True, port=5000) # Run the app in debug mode and on port 5000

    