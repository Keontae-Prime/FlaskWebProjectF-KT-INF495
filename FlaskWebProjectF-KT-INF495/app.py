"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from datetime import datetime
from flask import Flask,render_template,request
app = Flask(__name__)
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='My contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='My application description page.'
    )
@app.route('/',methods=['GET','POST'])
def myFunction():
    # Checks for request
    global user_input
    request.method=='POST'
    form=request.form
    while True:
        try:
            user_input=int(form['number'])
            message2="You entered", user_input
        except ValueError:
            message='Please enter an integer'
            return render_template("index.html",message=message)
        else:
            #Value was successfully parsed. Now the program can continue.
            #End loop.
            break
    #Returns the first proverb if the converted integer is 0
    if user_input==1:
        message="A bad workman always blames his tools. \nThis describes workers who can't take responsibility for their lack of effort."
    #Returns the second proverb if the converted integer is 1
    elif user_input==2:
        message="A cat has nine lives. \nThis means cats can survive seemingly fatal events."
    #Returns the third proverb if the converted integer is 2
    elif user_input==3:
        message="A chain is only as strong as its weakest link. \nThis means One weak person on a team makes the rest of the team weak."
    #Returns the fouth proverb if the converted integer is 3
    elif user_input==4:
        message="A drowning man will clutch at a straw. \nThis means that when our backs our against the wall, we will fight by any means necessary."
    #Returns the fifth proverb if the converted integer is 4
    elif user_input==5:
        message="Adversity and loss make a man wise. \nThis means you can learn from failure."
    #Returns the sixth proverb if the converted integer is 5
    elif user_input==6:
        message="A fool and his money are soon parted. \nThis means financially illiterate people can never be rich"
    #Returns the seventh proverb if the converted integer is 6
    elif user_input==7:
        message="All that glitters is not gold. \nThis means an outcome may look perfect, but the journey it took to get there was far from it."
    #Output
    #If the value is not an integer 
    elif user_input<1 or user_input>7:
        message='Number must be from 1-7'
    return render_template("index.html",message=message)

