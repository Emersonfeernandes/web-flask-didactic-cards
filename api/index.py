from flask import Flask

from routes.card import card_bp
from routes.main import main_bp
from routes.computer import computer_bp
from routes.read import read_bp

app = Flask(__name__)

app.register_blueprint(card_bp, url_prefix='/card')
app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(computer_bp, url_prefix='/computer-architecture')
app.register_blueprint(read_bp, url_prefix='/read')



if __name__ == '__main__':
    with app.app_context():
        print(app.url_map)
    app.run(debug=True)