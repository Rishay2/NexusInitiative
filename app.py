"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/campusmaps')
def campusmaps():
    return render_template('campusmaps.html')

@app.route('/studentreport')
def studentreport():
    return render_template('studentreport.html')

@app.route('/UpgradeLog')
def UpgradeLog():
    return render_template('UpgradeLog.htm')

@app.route('/MaintenanceReports')
def maintenance():
    return render_template('MaintenanceReports.html')

@app.route('/StudentViewReport')
def studentviewreport():
    return render_template('StudentViewReport.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
