from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faves')
def faves():
    players = [
        ['TOP 5 FAVORITE BASKETBALL PLAYERS', '1: Kevin Durant', '2: Devin Booker', '3: LeBron James', '4: Nikola Jokic', '5: Jayson Tatum'],
    ]
    return render_template('fav_five.html', player_list=players)