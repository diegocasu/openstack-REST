from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        CONTROLLER_IP='172.16.3.42',
        CONTROLLER_PORT='8080'
    )

    from . import images, schedules
    app.register_blueprint(images.bp)
    app.register_blueprint(schedules.bp)

    return app
