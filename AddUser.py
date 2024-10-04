import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Insert a new user
username = 'test'
password = 'test'
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# Save (commit) the changes and close the connection
conn.commit()
conn.close()

print("User added successfully!")
