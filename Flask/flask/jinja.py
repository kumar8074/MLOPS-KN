## Building Url Dynamically
## Variable rule
## Jinja 2 Template Engine

### Jinja 2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''


from flask import Flask, render_template, request

## WSGI Application
app=Flask(__name__) # It creates an instance of the Flask class, which will be your WSGI (web server gateway interface) application.

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask app</H1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}, Thanks for filling the form.'
    return render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}, Thanks for filling the form.'
    return render_template('form.html')


## Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
        
    exp={'score':score, 'res':res}
    return render_template('result1.html',results=exp)


# Building URL Dynamically
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)



if __name__ =="__main__":
    app.run(debug=True)