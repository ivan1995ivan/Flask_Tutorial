from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    movies = [
        {'title': 'The Shawshank Redemption', 'year': 1994, 'rating': 9.3},
        {'title': 'The Godfather', 'year': 1972, 'rating': 9.2},
        {'title': 'Pulp Fiction', 'year': 1994, 'rating': 4.9}
    ]
    return render_template('movies.html', movies=movies)

if __name__ == '__main__':
    app.run()