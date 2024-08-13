from flask import Flask, make_response, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return ""


@app.route('/sasi-team-members')
def sasi_team_members():
    response = make_response("sasi members!")
    response.set_cookie("admin", "True")
    return response


@app.route("/<slug>")
def qr_code_redirect(slug):
    admin = request.cookies.get("admin")
    if admin:
        return "admin member!"
    else:
        return redirect("https://wp.ovptl.uci.edu/sasi/")


if __name__ == "__main__":
    app.run(debug=True)
