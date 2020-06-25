from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        CONTROLLER_IP='openstackrest_api_1',
        CONTROLLER_PORT='8080'
    )

    from . import index, schedules
    app.register_blueprint(index.bp)
    app.register_blueprint(schedules.bp)

    return app
