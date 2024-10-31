from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hi, this is my first flask website</h1><br><a href='/user'>Go to the user page</a>"

@app.get("/user")
def user():
    return "this is the user page<br><a href='/'>and back again ;-) </a>"

if __name__ == '__main__': # if the script is executed directly, the code block is executed, if the script is imported, the code block is not executed.
    app.run(host='0.0.0.0', port='5070', debug = True) #specify the url and port, and debug = True allows for the server to automatically reload when changes are made to the code
    
