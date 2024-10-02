from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row  # This enables dictionary-like row access
    return conn

# Home route to display all expenses
@app.route('/')
def index():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Route to add an expense
@app.route('/add', methods=('GET', 'POST'))
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        
        if description and amount:
            conn = get_db_connection()
            conn.execute('INSERT INTO expenses (description, amount) VALUES (?, ?)',
                         (description, amount))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('index.html')

# Route to delete an expense
@app.route('/delete/<int:id>')
def delete_expense(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
