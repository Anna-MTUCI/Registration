from flask import Flask, render_template, request, redirect
import psycopg2

app=Flask(__name__)

@app.route('/login/', methods=['Get','POST'])
def index():
    if request.method=='POST':
        if request.form.get("login"):
            login = request.form.get('username')
            password = request.form.get('password')
            conn = psycopg2.connect(database = "service",user="postgres",password="1111",host="localhost",port="5432")
            cursor=conn.cursor()
            cursor.execute("SELECT name FROM shena_name.table_name WHERE login=%s and password=%s",
            (str(login), str(password)))
            records = list(cursor.fetchall())
            return render_template('account.html', full_name = records[0][1])
        if request.form.get("registration"):
            return redirect('/registration/')
    return render_template('login.html')
@app.route('/registration/', methods=['GET','POST'])
def registration():
    if request.method=='POST':
        name = request.form.get('name')
        login = request.form.get('username')
        password = request.form.get('password')
        conn = psycopg2.connect(database = "service",user="postgres",password="1111",host="localhost",port="5432")
        cursor=conn.cursor()
        cursor.execute("INSERT INTO users.user (name,login,pasword), VALUES (%s, %s, %s)"),
        (str(name), (str(login), str(password)))
        conn.commit()
        return redirect('/login/')

    return render_template('registration.html')
    
    