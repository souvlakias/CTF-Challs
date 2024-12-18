from flask import Flask, render_template, request, redirect, url_for, session, flash,make_response,send_from_directory
app = Flask(__name__)
from util import *


@app.route('/',methods=['GET'])
def home():
    if not request.cookies.get('token'):
        resp=make_response(render_template('index.html'))
        resp.set_cookie('token',make_cookie({'admin':False}))
        return resp
    return render_template('index.html')


@app.route('/robots.txt',methods=['GET'])
def robots():
    return send_from_directory('static','robots.txt')


@app.route('/error',methods=['GET'])
def error():
    return render_template('error.html')


@app.route('/panel',methods=['GET','POST'])
def panel():
    try:
        admin=is_admin(request.cookies.get('token'))
    except:
        admin=False
    if not admin:
        return render_template('error.html',message="Page is only for admins")
    if request.method=='POST':
        try:
            url=request.form['url']
            if not url.startswith('http'):
                url='http://'+url
            if not safe_input(url):
                return render_template('panel.html',error="Malicious input detected☹️")
            r=get(url).text
        except Exception as e:
            # print(e)
            return render_template('panel.html',error="Invalid input")
        return render_template('panel.html',data=r)
    return render_template('panel.html')

@app.route('/flag',methods=['GET'])
def flag():
    if request.remote_addr=='127.0.0.1':
        return render_template('flag.html')
    else:
        return render_template('error.html',message="The page is restricted from external access.")

@app.route('/<path:path>',methods=['GET'])
def catch_all(path):
    return render_template('error.html',message="Page not found")


if __name__ == '__main__':
    app.run(port=1337, threaded=True,debug=True,host='0.0.0.0')

 

