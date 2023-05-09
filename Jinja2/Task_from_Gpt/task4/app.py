from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    movie = {'title' : 'Titanic',
             'year' : 1998,
             'rating' : 9.9}
    return render_template('movie.html', **movie)

if __name__ == '__main__':
    app.run()