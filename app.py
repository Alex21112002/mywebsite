from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home Route to Display Login Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Route to Handle Login Submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check credentials in the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        flash(f"Welcome, {username}!", "success")
        return redirect(url_for('home'))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for('home'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
