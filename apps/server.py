from .simple_test import building_obj_file
import os
from flask import Flask, jsonify, send_file
from flask_restful import Resource, request, Api, reqparse

app = Flask(__name__)
api = Api(app)

# PATH_TEST_IMAGE = "C:/Users/Shachar/Desktop/Projects/hdProject/pifuhd/sample_images"
# PATH_OBJ_FILE = "C:/Users/Shachar/Desktop/Projects/hdProject/pifuhd/results/pifuhd_final/recon/result_test_512.obj"
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/obj-creation', methods=['POST'])
def create_obj():
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file and allowed_file(file.filename):
        file.save(os.path.join(request.form.get('local_path') + "/pifuhd/sample_images", "test.png"))
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        building_obj_file()
        return send_file(request.form.get('local_path') + "/pifuhd/results/pifuhd_final/recon/result_test_512.obj", mimetype='application/object')
    else:
        resp = jsonify({'message': 'Allowed file types are png, jpg'})
        resp.status_code = 400
        return resp

if __name__ == '__main__':
    app.run()



