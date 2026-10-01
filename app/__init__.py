from flask import Flask, render_template
from config import DevelopmentConfig
from .extensions import db,migrate
from .models import Expense


def create_app():

    app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

    app.config.from_object(DevelopmentConfig)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("500.html"), 500


    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    from .api import api
    app.register_blueprint(main)
    app.register_blueprint(api)


    return app
