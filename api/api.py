#%%
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class CreateData():
    def __init__(self, id, title, author, first_sentence, year_published):
        self.id = id
        self.title = title
        self.author = author
        self.first_sentence = first_sentence
        self.year_published = year_published

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["title"] = self.title
        data["author"] = self.author
        data["first_sentence"] = self.first_sentence
        data["year_published"] = self.year_published

        return data

books = [
    CreateData(0,
    'A Fire Upon the Deep',
    'Vernor Vinge',
    'The coldsleep itself was dreamless.',
    '1992').to_dict(),
    CreateData(1,
    'The Ones Who Walk Away From Omelas',
    'Ursula K. Le Guin',
    'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.'
    , '1973').to_dict(),
    CreateData(2,
    'Dhalgren',
    'Samuel R. Delany',
    'to wound the autumnal city.',
    '1975').to_dict()
    ]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
# %%
