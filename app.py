from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for session management

# Sample user data for demonstration
users = {
    "test": "test"
}

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Simple authentication check
    if username in users and users[username] == password:
        flash('Login successful!', 'success')
        return redirect(url_for('home'))  # Redirect to the home page or dashboard
    else:
        flash('Invalid username or password', 'danger')
        return redirect(url_for('home'))  # Redirect back to the login page

if __name__ == '__main__':
    app.run(debug=True)
