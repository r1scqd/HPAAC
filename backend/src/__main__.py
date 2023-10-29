from src.container import AppContainer
from .application import create_app

if __name__ == '__main__':
    app = create_app()
    app.config['SECRET_KEY'] = 'ucosuruonelove'
    container: AppContainer = app.container
    app.run(port=container.config.flask.port())
