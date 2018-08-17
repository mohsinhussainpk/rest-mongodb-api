from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todorest' 
app.config['MONGO_URI'] = 'mongodb://mohsin:password1@ds123852.mlab.com:23852/todorest'

mongo = PyMongo(app)


@app.route('/add')
def add():
    task = mongo.db.users
    task.insert({'name': 'Anthony'})
    return 'Added user 1'

if __name__ == '__main__':
    app.run(debug=True)