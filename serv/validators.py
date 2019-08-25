import re
from datetime import date, datetime


class InvalidRequestError(Exception):
    pass


def check_citizens(citizens):
    try:
        ids = set(citizens.keys())
        for i in citizens.keys():
            if len(citizens[i].keys()) > 9:
                raise InvalidRequestError
            if not all((
                        type(citizens[i]['citizen_id']) == int and citizens[i]['citizen_id'] >= 0,
                        check_pack(citizens[i]),
                        set(citizens[i]['relatives']).issubset(ids),
                        all((i in citizens[j]['relatives'] for j in citizens[i]['relatives']))
                    )):
                raise InvalidRequestError
    except (KeyError, ValueError):
        raise InvalidRequestError


def check_pack(data, auto_completion=False):
    pattern = r'[\d\w]'
    try:
        keys = {'town', 'street', 'building', 'apartment', 'name', 'birth_date', 'gender', 'relatives'}
        gag = {i: True for i in keys}
        booleans = []
        if auto_completion:
            gag.update({i: False for i in keys.difference(set(data.keys()))})

        if gag['town']:
            booleans.append(bool(re.match(pattern, data['town'])))
        if gag['street']:
            booleans.append(bool(re.match(pattern, data['street'])))
        if gag['building']:
            booleans.append(bool(re.match(pattern, data['building'])))
        if gag['apartment']:
            booleans.append(type(data['apartment']) == int and data['apartment'] >= 0)
        if gag['name']:
            booleans.append(0 < len(data['name']) <= 256)
        if gag['birth_date']:
            booleans.append(date(*[int(i) for i in data['birth_date'].split('.')][::-1]) <= datetime.today().date())
        if gag['gender']:
            booleans.append(data['gender'] in ('male', 'female'))

        if not all(booleans):
            raise InvalidRequestError
        else:
            return True

    except (KeyError, ValueError):
        raise InvalidRequestError

