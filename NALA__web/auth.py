from flask import render_template,Blueprint,request,redirect,flash,url_for,session
import re
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User
from . import db


auth = Blueprint('auth',__name__)

@auth.route('/register', methods=["POST","GET"])
def register():
    if request.method == "POST":
            username = request.form.get('username')
            emailAddress = request.form.get('email')
            password = request.form.get('password')
            cPassword = request.form.get('c-password')
            
            usernameChecker = User.query.filter_by(username=username).first()
            emailChecker = User.query.filter_by(emailAddress=emailAddress).first()
            
            if usernameChecker:
                flash("Username already taken!",category="error")
            elif emailChecker:
                flash("Email Address already taken", category="error")
            elif len(password) < 8 or bool(re.search("[0-9]",password)) == False or bool(re.search("(?=.*[ -\/:-@\[-\`{-~]{1,})",password)) == False:
                flash("Password must at least have 8 characters and have at least one number and one special characters", category="error")
            elif password != cPassword:
                flash("The Password you entered isn't the same as the Confirm Password", category="error")
            else:
                new_user = User(username=username,emailAddress=emailAddress,password=generate_password_hash(password,method="scrypt",salt_length=12))
                db.session.add(new_user)
                db.session.commit()
                flash("Account Created", category="success")
                return redirect(url_for('auth.login'))
                
    return render_template('register.html')
    

@auth.route('/login', methods=["POST","GET"])
def login():
    if "username" in session and session["accountType"] == "User":
            flash("Login Successfully" , category="success")
            return redirect(url_for('view.translatePage'))

    if "username" in session and session["accountType"] == "Admin":
            flash("Login Successfully" , category="success")
            return redirect(url_for('view.adminPage'))
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        usernameChecker = User.query.filter_by(username=username).first()
        print(usernameChecker)
        
        if usernameChecker:
            if check_password_hash(usernameChecker.password,password):
                session.permanent = True
                session["user_id"] = usernameChecker.id
                session["username"] = usernameChecker.username
                session["password"] = usernameChecker.password
                session["accountType"] = usernameChecker.account_type
                
                if "username" in session and session["accountType"] == "User":
                    flash("Login Successfully" , category="success")
                    return redirect(url_for('view.translatePage'))

                if "username" in session and session["accountType"] == "Admin":
                    flash("Login Successfully" , category="success")
                    return redirect(url_for('view.adminPage'))
                

            else:
                flash("Password is incorrect", category="error")        
        else:
            flash("No such thing as that username registered!", category="error")   
            
    return render_template('login.html')


@auth.route('/logout')
def logoutUser():
    session.pop("username",None)
    session.pop("password",None)
    session.pop("id",None)
    session.pop("accountType",None)
    flash("Log out Successfully", category="error")
    return redirect(url_for('auth.login'))

@auth.route('/delete/<int:id>')
def DeleteUser(id:int):
    delete_task = User.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect(url_for('view.adminPage'))
    except Exception as e:
        return f"ERROR{e}"   