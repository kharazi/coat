from flask import Flask, render_template
quote = Flask(__name__)

@quote.route('/')
def index():
    return render_template('index.html', name="quote")


@quote.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    quote.debug = True
    quote.run()