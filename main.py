from flask import Flask, render_template
from game_of_life import GameOfLife


app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(width=25, height=25)
    return render_template('index.html')


@app.route('/live')
def live():
    g = GameOfLife()
    g.form_new_generation()
    # print(g._GameOfLife__height)
    # print(g._GameOfLife__width)
    # print(g.world)
    return render_template('live.html', g=g)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
