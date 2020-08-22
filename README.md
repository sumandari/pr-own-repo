# Melakukan Pull Request pada repo sendiri 

## prequesition
- python3

## membuat dan mengkatifkan virtual environment 
```
$ python3 -m venv venv
$ source venv/bin/Activate
```

## install dependencies
```
$ pip install -r app/requirements.txt
```

## melakukan test dengan pytest
```
$ pytest -v app/test.py
```