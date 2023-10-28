import dataclasses

from dependency_injector.wiring import Provide
from flask import jsonify
from flask_restful import Resource, reqparse
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..container import AppContainer
from ..db.base import Database
from ..db.models import TariffModel
from ..resources.shared import abort_if_obj_not_found

parser = reqparse.RequestParser()

# required fields for post
for item in ('name', 'price', 'description'):
    parser.add_argument(item)


class SampleResource(Resource):
    def get(self):
        ...

    def post(self):
        ...

    def delete(self):
        ...
