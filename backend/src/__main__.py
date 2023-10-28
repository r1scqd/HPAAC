from .application import create_app

if __name__ == '__main__':
    app = create_app()
    app.config['SECRET_KEY'] = 'ucosuruonelove'
    app.run(port=8080)
