from flask import Flask, render_template

#creates WSGI
app=Flask(__name__)

#when we press / goes to yokoso page (should be home), default is also that page
@app.route("/")
def Welcome():
    return "<html><h1>This Is the heading for the page</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__=="__main__":
    #debug=True makes all changes live u only need to restart
    app.run(debug=True)
