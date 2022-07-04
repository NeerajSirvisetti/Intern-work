from flask import Flask,render_template,request,session
import pandas as pd
app = Flask(__name__)
app.config['SECRET_KEY']='password'
avail=0
selected=0
@app.route('/')
def home():
	session['avail']=avail
	session['selected']=selected

	return render_template('index.html')

@app.route('/feature')
def features():
    session['selected'] = request.args.get('last')
    return render_template('feature.html',selected=session['selected'],available=session['avail'])

@app.route('/dataset' , methods = ['GET', 'POST'])
def upload():
    file=request.files['fileupload']
    df=pd.read_csv(file)
    session['avail']=len(df.columns)
    return render_template('feature.html',selected=session['selected'],available=session['avail'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__=='__main__':
	app.run()