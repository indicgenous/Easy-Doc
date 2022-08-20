from flask import Flask , request , url_for , render_template 

app=Flask(__name__,template_folder='templates')


@app.route('/')
def home():
    return render_template('ff.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/show')
def show():
    return render_template('search.html') 

@app.route('/doc', methods=['POST','GET'])
def doc():
    loc=request.form['inp_loc']
    return render_template('doc.html',loc=loc)

@app.route('/des')
def des():
    return render_template('trigger.html')

@app.route('/test')
def med():
    return render_template("med.html")

if __name__=='__main__':
    app.run(debug=True)