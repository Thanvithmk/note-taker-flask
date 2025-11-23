from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    return render_template('login.html',text="Hello from login route")

@auth.route("/logout")
def logout():
    return render_template('logout.html')

@auth.route("/signup",methods=['GET','POST'])
def signup():

    if request.method=='POST':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email)<4:
            flash('Email must be greater than 4 characters.',category='error')
        elif len(password1)<7:
            flash('Password must be at least 7 characters.',category='error')
        elif password1!=password2:
            flash('Passwords don\'t match.',category='error')
        elif len(firstname)<2:
            flash('First name must be at least 2 characters.',category='error')
        else:
            flash('Account created!',category='success')
        
        print(email,password1,password2)

    return render_template('signup.html')

