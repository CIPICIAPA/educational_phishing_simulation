from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    return f"Ogłoszenie: {title}, Opis: {description}, Cena: {price}"

if __name__ == '__main__':
    app.run(debug=True)
