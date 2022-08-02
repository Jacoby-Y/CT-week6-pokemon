## Coding Temple Week 6 Pokemon Project
###### CT-week6-pokemon

#### Env variables
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY= —Hidden—
```

#### Create Secret Key
```python
 ~$ python # or python3 on Unix systems
>>> import secrets
>>> import secrets
>>> secrets.token_urlsafe(50)
# Copy output and paste as value for SECRET_KEY
```

#### Run Instructions
`$ python -m venv venv` - (python3 on Unix systems)   
`$ . venv/bin/activate`   
`$ pip install -r requirements.txt`   
`$ flask run`   
