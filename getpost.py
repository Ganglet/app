from flask import Flask, render_template, request

#creates WSGI
app=Flask(__name__)

#when we press / goes to yokoso page (should be home), default is also that page
@app.route("/")
def Welcome():
    return "<html><h1>This Is the heading for the page</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    #render_template is used to connect the python file to html
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def form():
    #get is bassicaly getting the info shown and post id giving the info to the site
    if request.method=='POST':
        pass
    return render_template("form.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        #bassicaly in the form page it asks info then redirects to submit page which displays the f string,
        #we also store the name part as name
        name=request.form['name']
        return f"Hello {name} how has you day been"
    return render_template("form.html")

if __name__=="__main__":
    #debug=True makes all changes live u only need to restart
    app.run(debug=True)
