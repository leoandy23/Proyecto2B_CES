from flask import Flask, request, jsonify
import personas

app = Flask(__name__)

@app.route('/persons', methods=['POST'])
def create_person():
    req_data = request.get_json()
    personas.create_person(
        req_data['name'],
        req_data['last_name'],
        req_data['age'],
        req_data['semester'],
        req_data['career']
    )
    return jsonify({"status": "Person created"}), 201

@app.route('/persons', methods=['GET'])
def get_persons():
    return jsonify(personas.get_persons()), 200

@app.route('/persons/<id>', methods=['GET'])
def get_person_by_id(id):
    return jsonify(personas.get_person_by_id(id)), 200

@app.route('/persons/<id>', methods=['PUT'])
def update_person(id):
    req_data = request.get_json()
    personas.update_person(id, req_data)
    return jsonify({"status": "Person updated"}), 200

@app.route('/persons/<id>', methods=['DELETE'])
def delete_person(id):
    personas.delete_person(id)
    return jsonify({"status": "Person deleted"}), 200

@app.route('/persons/semester/<semester>', methods=['GET'])
def get_person_by_semester(semester):
    return jsonify(personas.get_person_by_semester(semester)), 200

if __name__ == '__main__':
    app.run(debug=True)
