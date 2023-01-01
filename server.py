from flask import Flask
from connection import get_emp_firstname
import redis


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to employees database :"


@app.route('/get_emp_firstname')
def get_firstname():
    try:
        if r.exists('names'):
            print("hit")
            names = r.lrange('names', 0, -1)
            name_list = []
            for i in names:
                name_list.append(i.decode())
            return name_list
        else:
            print('miss')
            names = get_emp_firstname()
            for name in names:
                r.rpush('names', f'{name[0]}')
    except:
        names = get_emp_firstname()
        return names


if __name__ == '__main__':
    try:
        r = redis.Redis(host='localhost', port=6379)
    except:
        print("Redis server down")
    app.run(debug=True)
