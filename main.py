from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello HOME: " + os.environ['CONTAINER_NAME']

@app.route('/test')
def test():
    return "Hello TEST: " + os.environ['CONTAINER_NAME']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)