from flask import Flask, render_template
from .routes.api_routes import api_routes

def create_app():

    app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

    @app.route('/')
    def home_page():
        return render_template('index.html')
    
    @app.route('/backtest')
    def backtest_page():
        return render_template('backtest.html')

    @app.route('/login')
    def login_page():
        return render_template('login.html')

    @app.route('/learn')
    @app.route('/learn/<path:page>')
    def learn_page(page=None):
        if page:
            return render_template(f'learn/{page}.html')
        return render_template('learn.html')
    
    app.register_blueprint(api_routes)
    
    return app