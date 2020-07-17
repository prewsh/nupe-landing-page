from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import flash
# import yaml

app = Flask(__name__)

# Configure db
# db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = 'localhost'
# db['mysql_host']
app.config['MYSQL_USER'] = 'root'
# db['mysql_user']
app.config['MYSQL_PASSWORD'] = '1234'
# db['mysql_password']
app.config['MYSQL_DB'] = 'flaskapp'
# db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        email = userDetails['email'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(email) VALUES(%s)",[email])
        mysql.connection.commit()
        cur.close()  
        return redirect('/')
    return render_template('index.html')

@app.route('/subscribers')
def users(): 
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('subscribers.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
