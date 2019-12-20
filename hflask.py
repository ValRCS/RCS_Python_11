from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Sup!'

@app.route('/admin')
def admin():
    return 'Super Secret Admin Page'

@app.route('/about')
def about():
       user = {'username': 'Valdis'} 
       return '''
            <html>
                <head>
                    <title>Home Page - Microblog</title>
                </head>
                <body>
                    <h1>Hello, ''' + user['username'] + '''!</h1>
                </body>
            </html>'''

if __name__ == '__main__':
    app.run()
