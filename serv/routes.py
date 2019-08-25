from flask import request, Response
from serv import app, db, validators
from serv.validators import InvalidRequestError
import json


def resp(status_code, data=None):
    return Response(status=status_code,
                    mimetype='application/json',
                    response=json.dumps(data,
                                        indent=4,
                                        ensure_ascii=False) + "\n")


@app.route('/imports', methods=['POST'])
def set_import():
    try:
        data = request.get_json()
        data = {i['citizen_id']: i for i in data['citizens']}
        validators.check_citizens(data)
        import_id = db.add_import(data)
    except (InvalidRequestError, KeyError):
        return resp(400)
    return resp(201, {"data": {"import_id": import_id}})


@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def patch_user(import_id, citizen_id):
    data = request.get_json()
    try:
        validators.check_pack(data, auto_completion=True)
        user = db.patch_user(import_id, citizen_id, data)
    except InvalidRequestError:
        return resp(400)
    return resp(200, {"data": user})


@app.route('/imports/<int:import_id>/citizens', methods=['GET'])
def get_users(import_id):
    try:
        users = db.get_users(import_id)
        users = [users[i] for i in users.keys()]
    except InvalidRequestError:
        return resp(400)
    return resp(200, {"data": users})


@app.route('/imports/<int:import_id>/citizens/birthdays', methods=['GET'])
def get_birthdays(import_id):
    pass


@app.route('/imports/<int:import_id>/towns/stat/percentile/age', methods=['GET'])
def get_percentile(import_id):
    pass
