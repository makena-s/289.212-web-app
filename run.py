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
    justsent = []
    cur = db.execute('SELECT * FROM comments ORDER BY timestamp DESC LIMIT 1')
    for row in cur:
        justsent.append(list(row))
        
    return {'comments':comments, 'newest':newest, 'justsent':justsent} # python dictionary, made up of 'key names' and 'values'

@app.route('/')
def index():    
    con = sqlite3.connect(DOGDB)
    data = fetchData(con)
    con.close()
    
    print('hello world ;^)')
    print(sqlite3.connect(DOGDB)) # print in command prompt that connnection has worked
    return render_template('index.html',
                           disclaimer='open your mind to dog.',
                           newest=data['newest']
                          )

@app.route('/archive')
def archive():
    con = sqlite3.connect(DOGDB)
    data = fetchData(con)
    con.close()
    return render_template('archive.html',
                           disclaimer='your predecessors.',
                           comments=data['comments'],
                           newest=data['newest']
                          )

@app.route('/appraisal')
def appraisal():
    con = sqlite3.connect(DOGDB)
    data = fetchData(con)
    con.close()
    return render_template('appraisal.html',
                           disclaimer='divulge your truth.',
                           comments=data['comments'],
                           newest=data['newest']
                          )

@app.route('/confirm', methods=['POST'])
def confirm():
    details = {}
    con = sqlite3.connect(DOGDB)
    data = fetchData(con)

    for input in request.form:
        if input == 'commenttext' or input == 'username':
            details[input] = request.form[input]
       
    con = sqlite3.connect(DOGDB)
    cur = con.execute( 'INSERT INTO comments(username, commenttext) VALUES(?,?)', (details['username'], details['commenttext']))
    con.commit()
    con.close()

    return render_template('confirm.html',
                           details=details,
                           disclaimer='you have encountered dog.',
                           justsent=data['justsent']
                          )


@app.errorhandler(404) # custom 404 page
def page_not_found(e):
    return render_template('404.html', disclaimer='good gravy.'), 404









