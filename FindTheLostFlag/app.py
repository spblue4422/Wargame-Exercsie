from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('challenge.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, secret TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (id, username, password, secret) VALUES (1, 'admin', '**[NO!]**', '**[HERE_IS_THE_FLAG]**')")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, secret) VALUES (2, 'guest', 'guestpassword', 'Huh? Do you think the owner will give guests the flag? :)')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return '<h1>Welcome to the Secret Database</h1><p>Login to see your secrets.</p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect('challenge.db')
        c = conn.cursor()
        query = f"SELECT secret FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")

        try:
            c.execute(query)
            result = c.fetchone()
            if result:
                return f"<h1>Welcome, {username}!</h1><p>Your secret: {result[0]}</p>"
            else:
                return "<h1>Login failed</h1><p>Invalid username or password.</p>"
        except Exception as e:
            return f"<h1>Error</h1><p>{e}</p>"
        finally:
            conn.close()

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
