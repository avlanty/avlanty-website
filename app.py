from flask import Flask, render_template

app = Flask(__name__)

RNGINFO = [
    {
        'id':1,
        'title': 'Basketball'
    },
    {
        'id':2,
        'title': 'Whiskey',
        'type': 'Dog'
    },
    {
        'id':3,
        'title': 'Toyota 86',
        'price': '$20,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', rnginfo=RNGINFO)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)