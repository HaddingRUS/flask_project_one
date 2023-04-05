from flask import Flask, render_template
import config as config
from data import tours, departures

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departures/<departure>')
def departures_html(departure):
    length = 0
    list_price = []
    list_nights = []
    list_data = []
    for _, values in tours.items():
        if values['departure'] == departure:
            length += 1
            list_price.append(values['price'])
            list_nights.append(values['nights'])
    max_price = max(list_price)
    min_price = min(list_price)
    max_night = max(list_nights)
    min_night = min(list_nights)
    list_data.extend([length, max_price, min_price, max_night, min_night])
    return render_template('departure.html',
                           departure=departure, departures=departures,
                           tours=tours, list_data=list_data)


@app.route('/tours/<int:ids>')
def tours_web(ids):
    return render_template('tour.html', ids=ids, tours=tours, departures=departures)


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


if __name__ == '__main__':
    app.run()
