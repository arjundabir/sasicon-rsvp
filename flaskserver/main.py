"""
This is the main file for the flask server.
"""
from flask import Flask, make_response, request, redirect

app = Flask(__name__)


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
    if admin:
        return handle_slug(slug)
    else:
        return redirect("https://wp.ovptl.uci.edu/sasi/")


if __name__ == "__main__":
    app.run(debug=True)


def handle_slug(slug):
    """
    Handle the slug and return the appropriate response
    """
    return slug
