#!/usr/bin/env bash
sudo apt-get update
sudo apt-get upgrade
### PostgreSQL install ###
#wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - ;
#RELEASE=$(lsb_release -cs) ;
#echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main | sudo tee  /etc/apt/sources.list.d/pgdg.list ;
#sudo apt-get update
#sudo apt-get install postgresql-11 postgresql-server-dev-11
#sudo systemctl enable postgresql
sudo apt-get -y install python3.7 python3.7-dev python3.7-venv
sudo cp ./flask_api.service /etc/systemd/system/flask_api.service
python3.7 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
deactivate
sudo systemctl daemon-reload
sudo systemctl start flask_api
sudo systemctl enable flask_api
