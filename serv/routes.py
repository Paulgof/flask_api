from flask import abort, request, jsonify, Response
from serv import app, db, validators
import json


def resp(status_code, data):
    return Response(status=status_code,
                    mimetype='application/json',
                    response=json.dumps(data, ensure_ascii=False) + "\n",)


@app.route('/imports', methods=['POST'])
def set_import():
    data = request.get_json()
    # validator should be here
    import_id = db.add_import(data['citizens'])
    return resp(201, {"data": {"import_id": import_id}})


@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def patch_user(import_id, citizen_id):
    pass


@app.route('/imports/<int:import_id>/citizens', methods=['GET'])
def get_users(import_id):
    users = db.get_users(import_id)
    return resp(200, {"data": users})


@app.route('/imports/<int:import_id>/citizens/birthdays', methods=['GET'])
def get_birthdays(import_id):
    pass


@app.route('/imports/<int:import_id>/towns/stat/percentile/age', methods=['GET'])
def get_percentile(import_id):
    pass
