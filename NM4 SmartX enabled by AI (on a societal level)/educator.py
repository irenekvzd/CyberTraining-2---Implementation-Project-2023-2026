from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Here you can perform any processing with the data if needed
    return redirect('https://educator_chatbot.zapier.app')

if __name__ == '__main__':
    app.run(debug=True)
