from todo_app.data.item import Item
from flask.globals import request
from flask.helpers import url_for
from todo_app.data.items_mgmt import add_item, get_items, complete_item, delete_item, sort_items
from flask import Flask, render_template, redirect

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    item = Item(request.form.get('newItem'))
    item.add()

    Item.add('test name')
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    # complete_item(id)
    return redirect(url_for('index'))


@app.route('/delete/<id>')
def delete(id):
    delete_item(id)
    return redirect(url_for('index'))


@app.route('/sort/<order>')
def sort(order):
    sort_items(order)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
