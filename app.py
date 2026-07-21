from flask import Flask

app = Flask(__name__)

@app.route('/about')
def about():
    return "Hallo, selamat datang"

if __name__ == "__main__":
    app.run(debug=True)