"""Application module."""

from flask import Flask
from flask_restful import Api
from loguru import logger

from .container import AppContainer, get_inject_modules
from .db.models import TariffModel
from .resources.tariff import TariffResource, TariffsResource
from .resources.user import UserResource


def create_app() -> Flask:
    container = AppContainer()
    wm = get_inject_modules()
    logger.info(wm)
    container.wire(wm)

    db = container.db()
    db.create_database()

    app = Flask(__name__)
    app.container = container

    api = Api(app, '/api')

    api.add_resource(UserResource, '/user/<int:user_id>', '/user')
    api.add_resource(TariffResource, '/tariff/<int:tariff_id>', '/tariff')
    api.add_resource(TariffsResource, '/tariffs')
    return app
