from flask import Flask, render_template, request, redirect, url_for, session,flash,jsonify
app = Flask(__name__)
from util import *
app.secret_key=os.urandom(24)

@app.route('/')
def home():
    return redirect(url_for('register'))


@app.route('/<path:path>')
def catch(path):
    return f'Oops! No path {path}'

        
@app.route('/register',methods=["GET", "POST"])
def register(error_message=''):
    if request.method=='GET':
        return render_template('register.html',error_message=error_message)
    else:
        try:
            username=request.form['username']
            if username in users:
                flash('Username already taken')
                return redirect(url_for('register'))
            if len(username)>20:
                flash('Username too long')
                return redirect(url_for('register'))
            if not username.isalnum():
                flash('Username must be alphanumeric')
                return redirect(url_for('register'))
            n_len=int(request.form['n_length'])
            e=int(request.form['e'])
            key=make_key(n_len,e)
            session['private_key']=key.export_key().decode()
            session['public_key']=key.public_key().export_key().decode()
            session['username']=username
            add_user(username,key)  
            return redirect(url_for('chats'))
        except Exception as e:
            session.clear()
            flash('Invalid Request')
            print(e)
            return redirect(url_for('register'))

@app.route('/chats',methods=["GET", "POST"])
def chats():
    if 'username' not in session:
        flash('Please register first')
        return redirect(url_for('register'))
    if request.method=='GET':
        return render_template('chats.html',messages=messages,current_user=session['username'])
    else:
        try:
            message=request.form['message']
            messages.append((session['username'],message))
            return redirect(url_for('chats'))
        except:
            flash('Invalid Request')
            return redirect(url_for('chats'))
        
@app.route('/secrets',methods=["GET", "POST"])
def secrets():
    if 'username' not in session:
        flash('Please register first')
        return redirect(url_for('register'))
    if request.method=='GET':
        new_secrets=[(sender,receiver,f'{c}',f'Decrypted message: {dec_message(c,users[receiver])}') if receiver==session['username'] or sender==session['username'] else (sender,receiver,f'{c}','') for sender,receiver,c in secret_messages ]
        return render_template('secrets.html',secrets=new_secrets,current_user=session['username'],users=users)
    else:
        try:
            message=request.form['message']
            recipient=request.form['recipient']
            if recipient not in users:
                flash('Invalid recipient')
                return redirect(url_for('secrets'))
            secret_messages.append((session['username'],recipient,enc_message(message,users[recipient])))
            return redirect(url_for('secrets'))
        except:
            flash('Invalid Request')
            return redirect(url_for('secrets'))
    
    
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('register'))


@app.route('/users')
def all_users():
    if 'username' not in session:
        flash('Please register first')
        return redirect(url_for('register'))
    return render_template('users.html',users=[(username,users[username].public_key().export_key().decode()) for username in users.keys()])

@app.route('/users/<username>')
def user(username):
    if 'username' not in session:
        flash('Please register first')
        return redirect(url_for('register'))
    if username not in users:
        return redirect(url_for('all_users'))
    return render_template('users.html',users=[(username,users[username].public_key().export_key().decode())])

@app.route('/profile')
def profile():
    if 'username' not in session:
        flash('Please register first')
        return redirect(url_for('register'))
    return render_template('profile.html',username=session['username'],private_key=session['private_key'])


if __name__ == '__main__':
    app.run(debug=True)
