from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection, create_table

create_table()
app = Flask(__name__)
app.secret_key = "rahasia123" 

@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY id")
    users = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template("index.html", users=users)

@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    
    if name:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        cur.close()
        conn.close()
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users ORDER BY id")
        users = cur.fetchall()
        cur.close()
        conn.close()
        
        
        return render_template("index.html", users=users, success_message=f"User '{name}' added successfully!")
    
   
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)