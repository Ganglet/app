from flask import Flask

#creates WSGI
app=Flask(__name__)

#when we press / goes to yokoso page (should be home), default is also that page
@app.route("/")
def Welcome():
    return "Welcome to the page"

@app.route("/index")
def index():
    return "This is the index page"

@app.route("/test")
def test():
    return "This is a test page"

if __name__=="__main__":
    #debug=True makes all changes live u only need to restart
    app.run(debug=True)