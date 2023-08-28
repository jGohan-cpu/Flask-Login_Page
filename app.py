from flask import (
    Flask,
    render_template
)


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Jose', password='secret'))

print(users[1].id)

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')
