from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'ojhj090e9fwiorj908sd0foijhklfdgf'
DOGDB = 'sqlite/dog.db'

def fetchData(con):
    db = sqlite3.connect(DOGDB) # connect to database
    comments = []
    cur = db.execute('SELECT * FROM comments')
    for row in cur:
        comments.append(list(row))
        
    newest = []
    cur = db.execute('SELECT * FROM comments ORDER BY timestamp DESC LIMIT 3')
    for row in cur:
        newest.append(list(row))
        
    return {'comments':comments, 'newest':newest} # python dictionary, made up of 'key names' and 'values'

@app.route('/')
def index():    
    con = sqlite3.connect(DOGDB)
    data = fetchData(con)
    con.close()
    
    print('hello world ;^)')
    print(sqlite3.connect(DOGDB)) # print in command prompt that connnection has worked
    
    return render_template('index.html',
                           disclaimer='disclaimer, babey!',
                           comments=data['comments'],
                           
                           newest=data['newest'
                           ]
                          )










































