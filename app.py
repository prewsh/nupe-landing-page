from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import flash 
# import yaml

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# app = Flask(__name__)

# Configure db
# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = 'us-cdbr-east-02.cleardb.com hostname'
# db['mysql_host']
# app.config['MYSQL_USER'] = 'b9666506382db7'
# db['mysql_user']
# app.config['MYSQL_PASSWORD'] = '02166bcf'
# db['mysql_password']
# app.config['MYSQL_DB'] = 'flaskapp'
# db['mysql_db']

# mysql = MySQL(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self ):
        return "< task %r>" %self.id

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Fetch form data
#         userDetails = request.form
#         email = userDetails['email'] 
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(email) VALUES(%s)",[email])
#         mysql.connection.commit()
#         cur.close()  
#         return redirect('/')
#     return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task_content = request.form['email']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'An error occured while adding Task'
            pass

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


# @app.route('/subscribers')
# def users(): 
#     cur = mysql.connection.cursor()
#     resultValue = cur.execute("SELECT * FROM users")
#     if resultValue > 0:
#         userDetails = cur.fetchall()
#         return render_template('subscribers.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
