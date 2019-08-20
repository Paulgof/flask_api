from flask import abort, request, jsonify
from serv import app
from serv.models import Data


@app.route('/imports', methods=['POST'])
def set_import():
    data = request.get_json()
    return jsonify(data)

@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def patch_user(import_id, citizen_id):
    pass


@app.route('/imports/<int:import_id>/citizens', methods=['GET'])
def get_users(import_id):
    pass


@app.route('/imports/<int:import_id>/citizens/birthdays', methods=['GET'])
def get_birthdays(import_id):
    pass


@app.route('/imports/<int:import_id>/towns/stat/percentile/age', methods=['GET'])
def get_percentile(import_id):
    pass
