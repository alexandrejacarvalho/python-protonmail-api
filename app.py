from flask import Flask, jsonify
from crawlers.inbox import *

app = Flask(__name__)


@app.route('/inbox/get/<int:page>', methods=['GET'])
def inbox_get_page(page=None):
    emails = inbox_get_by_page(page)

    return jsonify(emails)


@app.route('/')
def hello_world():
    return ''


if __name__ == '__main__':
    app.run(debug=True)
