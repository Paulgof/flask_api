from serv import db


class Data(db.Model):
    import_id = db.Column(db.Integer, index=True)
    citizen_id = db.Column(db.Integer, index=True)
    town = db.Column(db.VARCHAR(256), index=True)
    street = db.Column(db.VARCHAR(256))
    building = db.Column(db.VARCHAR(256))
    apartment = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(256))
    birth_date = db.Column(db.DATE, index=True)
    gender = db.Column(db.VARCHAR(8))
    relatives = db.Column(db.ARRAY(db.Integer), )
    db.PrimaryKeyConstraint(import_id, citizen_id)
