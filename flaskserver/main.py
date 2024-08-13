"""
This is the main file for the flask server.
"""
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, make_response, request, redirect
from sheetsapi.event_attendance.main import add_to_event
from sheetsapi.individual_attendance.main import add_to_individual_attendance


app = Flask(__name__)


def handle_slug(slug):
    """
    Handle the slug and return the appropriate response
    """
    name = slug.replace("-", " ").title()
    add_to_event(event_name="Conference", name=name)
    add_to_individual_attendance(name=name)
    return name


@app.route('/')
def home():
    """
    Return the home page
    """
    return ""


@app.route('/sasi-team-members')
def sasi_team_members():
    """
    Set the cookie to "True" and redirect to the sasi team members page
    """
    response = make_response("sasi members!")
    response.set_cookie("admin", "True")
    return response


@app.route("/<slug>")
def qr_code_redirect(slug):
    """
    Redirect to the sasi team members page if the admin cookie is set
    """
    admin = request.cookies.get("admin")
    admin = bool(admin)
    if admin:
        return handle_slug(slug)
    else:
        return redirect("https://wp.ovptl.uci.edu/sasi/")


if __name__ == "__main__":
    app.run(debug=True)