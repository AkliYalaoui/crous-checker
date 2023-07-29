# Crous checker
A python script that checks for update in the crous website

# Installation
First please setup a python virtual env and activate It :
```console
python -m venv env
```

Then install dependencies : 
```console
pip install -r requirements.txt
```

Create a .env file with these keys : 
```console
bounds=
url=
smtp_server=
smtp_port=
sender_email=
sender_password=
```

Launch the script : 
```console
python main.py
```