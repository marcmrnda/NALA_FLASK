from flask import render_template,Blueprint,session,redirect,url_for,flash
from .model import User

view = Blueprint("view", __name__)

@view.route('/')
def home():
    return render_template("index.html")


@view.route('/translation-page')
def translatePage():
    if not "username" in session:
        flash("Need to login to access the site", category="error")
        return redirect(url_for("auth.login"))
    if session["accountType"] != "User":
        return redirect(url_for("view.forbidden")) 
    return render_template("translation.html")


@view.route('/admin')
def adminPage():    
    if not "username" in session:
            flash("Need to login to access the site", category="error")
            return redirect(url_for("auth.login"))
    if session["accountType"] != "Admin":
        return redirect(url_for("view.forbidden"))    
    query = User.query.all()
    return render_template('admin.html' , query=query)


@view.route('/unified')
def unifiedPage():
    if not "username" in session:
        flash("Need to login to access the site", category="error")
        return redirect(url_for("auth.login"))
    if session["accountType"] != "User":
        return redirect(url_for("view.forbidden")) 
    return render_template("unified.html")
    

@view.route('/unauthorized')
def forbidden():
    return render_template("403.html")

