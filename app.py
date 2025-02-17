from flask import Flask, render_template

application = Flask(__name__)

projects = [
    {
        "title": "SpareChange - Real Estate App",
        "description": "A Flask-based real estate listing platform.",
        "tech": "Flask, Python, SQLite, Firebase",
        "link": "https://solaire.cs.csub.edu/gitlab/sparechange/sparechange/-/tree/main/backend?ref_type=heads"
    },
    {
        "title": "GoldRushLite - Game",
        "description": "A game developed in C using Windows X11.",
        "tech": "C, X11",
        "link": "https://github.com/braden-ca/Goldrush-Lite"
    }
]

@application.route('/projects')
def project_page():
    return render_template('projects.html', projects = projects)

@application.route('/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    application.run(debug=True)