from flask import Flask, render_template

application = Flask(__name__)


@application.route('/projects')
def project_page():
    return render_template('projects.html')


@application.route('/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    application.run(debug=True)