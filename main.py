from flask import Flask, request
from datetime import datetime


app = Flask('My first application')

@app.route('/')    #help user to get what he/she requested 
def index():
    return ''''
    <h1>MY FIRST WEBSITE ABOUT FLASK!!</h1>
    <button>What's your name</button>
    <body>My name is Miguel</body>
    '''

    

    # 'Hello, this is the front page of my website, and its very attractive'


@app.route('/Nyandikira')    #help user to get what he/she requested 
def contact_page():
    return 'Contact me through : fabienmiguel@gmail.com or +250 788689309'


@app.route('/date')
def show_page():
    date = str(datetime.now())
    return f'Today is {date}'  


@app.route('/birthyear', methods=['POST','GET'])
def calc_birthyear():
    if request.method == 'POST': # User is pointing or submitting his/her information
        return f"""<form action ="/birthyear" method ="POST">  
        <input type = "number" name ="birthyear" placeholder = "Birthyear e.g 2020"></input>
        <button type = "submit" value = "submit"> submit</button>
        </form>
                from your submition your age is: {2022 -  int(request.form.get('birthyear'))}"
             """
       
    elif request.method == 'GET': #User is asking for this page
          
        return """
        <form action ="/birthyear" method ="POST">  
        <input type = "number" name ="birthyear" placeholder = "Birthyear e.g 2020"></input>
        <button type = "submit" value = "submit"> submit</button>
        </form>
        """


if __name__ == '__main__':
    app.run()