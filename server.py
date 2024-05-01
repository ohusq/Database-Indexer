from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    search_value = request.args.get('search')
    select_value = request.args.get('select')

    if not search_value or not select_value:
        return "No search parameters provided"

    conn = sqlite3.connect('credentials.db')
    c = conn.cursor()

    if select_value == "username":
        c.execute("SELECT * FROM Users WHERE Username = ?", (search_value,))
        results = c.fetchall()
    elif select_value == "password":
        c.execute("SELECT * FROM Users WHERE Password = ?", (search_value,))
        results = c.fetchall()
    else:
        conn.close()
        return "Invalid search parameter", 400

    conn.close()
    
    # Render HTML template with search results
    return render_template("search_results.html", results=results)

if __name__ == '__main__':
    app.run(host='', port=5000, debug=False)
