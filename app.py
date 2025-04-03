from flask import Flask, render_template

application = Flask(__name__)
# Configure for production with your domain
application.config['SERVER_NAME'] = 'bradensmelser.com'

projects = [
    {
        "title": "SpareChange - Real Estate App",
        "description": "A modern real estate platform with an integrated mortgage calculator, built using Flask and Firebase. This application allows users to browse properties, calculate mortgage options, and save favorite listings.",
        "tech": "Flask, Python, Firebase, SQLite, JavaScript",
        "link": "https://solaire.cs.csub.edu/gitlab/sparechange/sparechange/-/tree/main/backend?ref_type=heads",
        "image": "static/images/real-estate.jpg"
    },
    {
        "title": "GoldRushLite - Game",
        "description": "An interactive 2D game developed in C using Windows X11 graphics library. Features include a game timer, score counter, and realistic collision mechanics for an engaging player experience.",
        "tech": "C, X11, Graphics Programming",
        "link": "https://github.com/braden-ca/Goldrush-Lite",
        "image": "static/images/game.jpg"
    },
    {
        "title": "Social Media Platform",
        "description": "A full-featured social media application with user authentication, post creation, commenting, and profile management. Developed with a responsive design for cross-platform compatibility.",
        "tech": "HTML/CSS, JavaScript, Python, Database",
        "link": "#",
        "image": "static/images/social-media.jpg"
    },
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio website showcasing my projects and skills. Built with responsive design and modern web technologies, featuring smooth animations and a clean user interface.",
        "tech": "HTML/CSS, Bootstrap, JavaScript, Flask",
        "link": "#",
        "image": "static/images/portfolio.jpg"
    }
]

@application.route('/projects')
def project_page():
    return render_template('projects.html', projects=projects)

@application.route('/')
def about():
    return render_template('about.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # For development
    application.config['SERVER_NAME'] = None
    application.run(host='0.0.0.0', port=80)