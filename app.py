import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'This is the new Docker message! Your docker container is set up!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
