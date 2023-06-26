from flask import Flask, json, render_template, request
from helpers import data_scraper

app = Flask(__name__)


@app.route('/')
def get_page_index():
    return render_template('index.html'), 200


@app.route('/cours')
def get_page_cours():
    return render_template('choix_cours_template.html'), 200


#  Search by program ID, redirects to list of courses, else back
#  to page with error message
@app.route('/programme', methods=['GET'])
def get_programme():
    semester = request.args.get('semester')  # get inputs from form
    program_id = request.args.get('program_id')
    program_title = request.args.get('program_title')
    program_title = "PROGRAM_TITLE_PLACEHOLDER"
    # Empty parameters validation
    if not semester or not program_id or not program_title:
        error = "Le champs ne peut pas etre vide."
        return render_template("index.html", error=error), 400
    list = data_scraper.get_program_courses(program_id)
    # empty list validation
    if list == "[]":
        error = "Entrez un nom de programme valide."
        return render_template("index.html", error=error), 400
    list = json.loads(list)
    return render_template('choix_cours.html', courses=list,
                           title=program_title, semester=semester), 200
