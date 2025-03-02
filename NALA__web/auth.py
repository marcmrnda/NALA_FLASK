from flask import render_template,Blueprint,request,redirect,flash,url_for,session,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User
from . import db
from flask_cors import CORS
import requests


auth = Blueprint('auth',__name__)


CORS(auth, resources={r"/*": {"origins": "http://127.0.0.1:5000/"}})


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
                session["username"] = usernameChecker.username
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
    session.clear()
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

@auth.route('/translate', methods=["POST", "GET"])
def translatePage():
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Get the input text from the form
        inputText = request.form.get("textInput")  

        # Get the selected language pair (e.g., "eng_to_ceb")
        inputLanguages = request.form.get("languageInput")  

        # Get the target output language (e.g., "ceb")
        outputLanguage = request.form.get("languageOutput") 

        # Extract the source language by removing "_to_" from the value
        inputLanguage = inputLanguages.replace("_to_", "")

        # Construct the Google Translate API URL
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={inputLanguage}&tl={outputLanguage}&dt=t&q={requests.utils.quote(inputText)}"

        # Send a request to the Google Translate API
        response = requests.get(url)

        # Parse the JSON response from the API
        data = response.json()

        # Extract the translated text from the API response
        translated = data[0][0][0]

        # If the request is made via AJAX (for live translation), return JSON response
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"translatedText": translated, "inputText": inputText})

    # If GET request or no AJAX request, render the translation page normally
    return render_template('translation.html')
