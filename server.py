from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key = 'pineapple'

@app.route('/')
def home():
    return redirect('/read')

@app.route('/read')
def users():
    users=User.get_all()
    return render_template('read.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/new_user', methods=['post'])
def newUser():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    user = User.select_last()
    for user in user:
        id = str(user['id'])
    return redirect('/user/' + id)

@app.route('/user/<int:id>')
def user_page(id):
    user=User.select(id)
    if 'id' not in session:
        session['id'] = id
    else:
        session['id'] = id
    return render_template('user.html', user=user)

@app.route('/edit/<int:id>')
def edit_page(id):
    user=User.select(id)
    if 'id' not in session:
        session['id'] = id
    else:
        session['id'] = id
    return render_template('edit.html', user=user)

@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/read')

@app.route('/update', methods=['post'])
def updates():
    data = {
        "id": int(session['id']),
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    id = str(session['id'])
    User.update(data)
    return redirect('/user/' + id)


if __name__ == '__main__':
    app.run(debug=True)