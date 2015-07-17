from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page. <br><a href='/hello'>Click Me!</a>"


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", ninja=player, niceword=compliment)


@app.route('/game')
def show_game_form():
    player_answer = request.args.get("game")

    if player_answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    select_person = request.args.get("person")
    select_color = request.args.get("color")
    select_noun = request.args.get("noun")
    select_adj = request.args.get("adjective")

    return render_template("madlib.html", person = select_person, color = select_color, noun = select_noun, adjective = select_adj)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
