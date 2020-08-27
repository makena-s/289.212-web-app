from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'ojhj090e9fwiorj908sd0foijhklfdgf'
DOGDB = 'sqlite/dog.db'

def fetchData(con):
    db = sqlite3.connect(DOGDB) # connect to database
    
    comments = []
    cur = db.execute('SELECT * FROM comments ORDER BY timestamp DESC')
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
                           newest=data['newest']
                          )

@app.route('/archive')
def archive():
    con = sqlite3.connect(DOGDB)
    data = fetchData(con)
    con.close()
    return render_template('archive.html',
                           disclaimer='appraise dog.',
                           comments=data['comments'],
                           newest=data['newest']
                          )


@app.errorhandler(404) # custom 404 page
def page_not_found(e):
    return render_template('404.html', disclaimer='good gravy!'), 404







































