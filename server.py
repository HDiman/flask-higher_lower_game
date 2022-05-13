from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
