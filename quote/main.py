from flask import Flask, session, redirect, url_for, escape, request, render_template

quote = Flask(__name__)

@quote.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', name=session['username'])
    else:
        return render_template('index.html', name='Not Session')


@quote.route('/login', methods=['GET', 'POST'])
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

@quote.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:

@quote.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    quote.secret_key = 'ThisIsVeryVeryHard'
    quote.debug = True
    if quote.debug:
        from lesscss import LessCSS
        LessCSS(media_dir='static/css', based=False)
    quote.run()