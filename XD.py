from flask import Flask, render_template, redirect, url_for, flash
from forms import SignUpForm
from forms import loginForm

error = "INVALID"
app=Flask(__name__)
app.config['SECRET_KEY'] = 'password'
@app.route('/')
def index():
    message = "This is Home Page!"
    return render_template("index.html", message=message)

@app.route('/about')
def about():
    message = "This is About Page!"
    return render_template("about.html", message=message)

@app.route('/contactus')
def contactUs():
    message = "This is Contact Us Page!"
    return render_template("contactUs.html", message=message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('You Have Successfully Registered, Please Log In!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == "aadesh.gavhane100@gmail.com" and form.password.data == "123":
            flash('Logged In!')
            return redirect(url_for("index"))

        else:
            message = "Incorrect email or password"
            return render_template('login.html', form=form, message=message)
            
    return render_template("login.html", form=form)

if __name__=='__main__':
    app.run(debug=True)