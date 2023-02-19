from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

# Load the best matches JSON file
with open('results.json', 'r', encoding='utf-8') as json_file:
    best_matches = json.load(json_file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    # Get the search query from the form
    query = request.form['query']

    # Get the best matches for the query
    matches = best_matches.get(query, [])

    # Render the search results template with the matches
    return render_template('search_results.html', query=query, matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
