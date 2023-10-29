"""Application module."""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from loguru import logger

from .container import AppContainer, get_inject_modules
from .db.models import TestSessionModel
from .resources.organization import OrganizationResource, OrganizationsResource
from .resources.tariff import TariffResource, TariffsResource
from .resources.test_session import TestSessionResource, TestsSessionResource
from .resources.tests import TestResource, TestsResource, VrResource, VrsResource
from .resources.user import UserResource, UsersResource, UserSignin


def create_app() -> Flask:
    container = AppContainer()
    wm = get_inject_modules()
    logger.info(wm)
    container.wire(wm)

    db = container.db()
    db.create_database()

    app = Flask(__name__)
    app.container = container

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    api = Api(app, '/api')

    api.add_resource(UserResource, '/user/<int:id>', '/user')
    api.add_resource(UsersResource, '/users')
    api.add_resource(TariffResource, '/tariff/<int:id>', '/tariff')
    api.add_resource(TariffsResource, '/tariffs')

    api.add_resource(TestResource, '/test/<int:id>', '/test')
    api.add_resource(TestsResource, '/tests')

    api.add_resource(VrResource, '/vr/<int:id>', '/vr')
    api.add_resource(VrsResource, '/vrs')

    api.add_resource(OrganizationResource, '/organization/<int:id>', '/organization')
    api.add_resource(OrganizationsResource, '/organizations')

    api.add_resource(TestSessionResource, '/testsession/<int:id>', '/testsession')
    api.add_resource(TestsSessionResource, '/testsessions')

    api.add_resource(UserSignin, '/signin')
    return app
