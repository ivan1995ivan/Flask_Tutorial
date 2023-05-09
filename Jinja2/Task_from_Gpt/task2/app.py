from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    products = [
        {'name': 'Хлеб', 'price': 10.99, 'description': 'Белый, нарезаный хлеб'},
        {'name': 'Сметана', 'price': 19.99, 'description': 'жирность 15%'},
        {'name': 'Соль', 'price': 5.99, 'description': '1кг'}
    ]
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run()