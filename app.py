from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

 # This will store the string received from the POST request
data_store = {"data": None}

@app.route('/store', methods=['POST'])
def store_data():
        data = request.get_json()
        data_store["data"] = data.get('data', None)
        return jsonify({"message": "Data stored successfully"}), 200

@app.route('/receive', methods=['GET'])
def receive_data():
        is_data_present = data_store["data"] is not None
        return jsonify({"data_present": is_data_present
        ,
        "data": data_store}), 200

latest_image = None

@app.route('/stream', methods=['POST'])
def post_image():
    global latest_image
    latest_image = request.data  # Get the image data
    # Now you can save the image or process it as needed
    return 'Image received', 200

@app.route('/latest', methods=['GET'])
def get_image():
    global latest_image
    if latest_image is None:
        return 'No image available', 404
    else:
        #return send_file(io.BytesIO(latest_image), mimetype='image/jpeg')
        return latest_image, 200