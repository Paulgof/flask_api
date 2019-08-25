#!/usr/bin/env bash
source /home/entrant/dev/flask_api/env/bin/activate
exec gunicorn -b 0.0.0.0:8080 -w 9 app:app