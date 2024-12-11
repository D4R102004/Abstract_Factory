from flask import Flask
app = Flask(__name__)

class AbstractFactory:
    def __init__(self):
        self._p = 3
    @property
    def p(self):
        return self._p
    
@app.route('/')
@app.route('/home')
def home_page():
    
