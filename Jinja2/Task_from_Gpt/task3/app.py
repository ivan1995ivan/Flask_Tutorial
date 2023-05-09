from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "John"
    age = 25
    city = "New York"
    return render_template('variables.html', name=name, age=age, city=city)

if __name__ == '__main__':
    app.run()