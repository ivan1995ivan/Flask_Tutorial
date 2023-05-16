from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/products')
def products():
    products = ['Product1', 'Product2', 'Product3']
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run()