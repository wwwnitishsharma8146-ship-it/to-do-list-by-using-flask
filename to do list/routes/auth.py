from flask import Blueprint, render_template, redirect, url_for, flash, session, request
auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': '123'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            session["user"] = username
            flash("login successful", "success")
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("invalid credentials", "danger")
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop("user",None)
    flash("logged out successfully","info")
    return redirect(url_for('auth.login'))