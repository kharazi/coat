from flask import Flask

quote = Flask(__name__)

@quote.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    quote.debug = True
    quote.run()