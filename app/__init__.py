from flask import Flask, render_template
from config import DevelopmentConfig



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


    from .routes import main
    app.register_blueprint(main)


    return app

