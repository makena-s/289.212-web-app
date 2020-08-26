from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'ojhj090e9fwiorj908sd0foijhklfdgf'
DOGDB = 'dog.db'

def fetchMenu(con):
    db = sqlite3.connect(DOGDB) # connect to database
    print(db) # print in console that connnection has worked, <sqlite3.Connection object at 0x7fd7d84db300>
    print('egg')

@app.route('/')
def index():
    con = sqlite3.connect('dog.db')
    cur = con.execute('SELECT * FROM comments')
    
#    for row in cur:
#        comments.append(list(row))
        
    con.close()
    return('<h1>dog blog</h1>')