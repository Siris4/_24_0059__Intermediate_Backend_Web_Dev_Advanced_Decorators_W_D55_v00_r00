from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "Hello Flask!"

# Remember: This is a Decorator function, which lives inside the app Object, which is declared in the Flask Class.
@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")   # if you want 'Freddy/5' to actually be the name itself, then we would just have the /5 be part of the name with it, and since it has a / in front of it (in a string), we use path type to process this:
def greet(name, number):
    return f'<h1 style="text-align: center">Hello {name}, you are {number} ' \
           f'years old!!</h1><p>This is a paragraph.</p>' \
           f"<img src='https://media.giphy.com/media/Puc4FZWExJc0E/giphy.gif?cid=790b7611gyi3ava1jsb6pg0r99pmhenwo3wjib7f3x7xt0en&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400>"


@app.route("/<name>")
def greet2(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)
