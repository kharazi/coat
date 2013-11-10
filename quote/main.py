from flask import Flask, session, redirect, url_for, escape, request, render_template, Response
from flask.ext import restful
from flaskext.gravatar import Gravatar
from session_interface import RedisSessionInterface


app = Flask(__name__)
api = restful.Api(app)

app.session_interface = RedisSessionInterface()

gravatar = Gravatar(
    app,
    size=25,
    rating='g',
    default='retro',
    force_default=False,
    force_lower=False
)


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', name=session['username'])
    else:
        return render_template('index.html', name='Not Session')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


class HelloWorld(restful.Resource):

    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')


if __name__ == '__main__':
    app.secret_key = 'ThisIsVeryVeryHard'
    app.debug = True
    if app.debug:
        from lesscss import LessCSS
        LessCSS(media_dir='static/css', based=False)
    app.run()
