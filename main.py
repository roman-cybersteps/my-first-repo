from flask import Flask, session, redirect, url_for

from flask_session import Session 

app = Flask(__name__)
app.secret_key = 'mysecretkey'

#  Configure server-side session
app.config['SESSION_TYPE'] = 'filesystem'  # Could be 'redis', 'mongodb', etc.
Session(app)

@app.route('/')
def index():
    cart = session.get('cart', [])
    items = '<br>'.join(cart) or 'Cart is empty.'
    return f"""
        <h2>Your Cart (Server-Side Session)</h2>
        {items}<br><br>
        <a href="/add/Apple">Add Apple</a> |
        <a href="/add/Banana">Add Banana</a> |
        <a href="/clear">Clear Cart</a>
    """

@app.route('/add/<item>')
def add(item):
    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)