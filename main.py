from flask import Flask,render_template,request,session,flash
import pandas as pd
import cls as cl
import sl
import os

app = Flask(__name__)
app.config['SECRET_KEY']='password'
avail=0
selected=0
@app.route('/')
def home():
	session['dataset']= None

	return render_template('index.html')

@app.route('/status', methods = ['GET', 'POST'])
def status():
    if request.method == "POST":
        session['dataset']= request.form['dataset']
        k = len(session['dataset'])
        session['state'] = request.form['feature_status']
        session['feature_selector'] = request.form['feature_selectors']
        session['classifier'] = request.form['classifiers']
        session['rank'] = request.form['ranks']
        if k!=0:
            if session['state'] == "enable":
                n=sl.filter(session['feature_selector'],session['dataset'])
                acc=cl.model(session['dataset'],session['classifier'])
                flash("You just uploaded the {} file!\n The important features of the given dataset in descending order are {}".format(session['dataset'],n))
            #print(state,feature_selector,classifier,rank,dataset)
            else:
                acc=cl.model(session['dataset'],session['classifier'])
                flash("You just uploaded the {} file!".format(session['dataset']))
            return render_template('data.html', classifier = session['classifier'] , acc = acc)

        else:
            return render_template('404.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__=='__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)