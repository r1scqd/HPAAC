import flask
from dependency_injector.wiring import inject, Provide
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from loguru import logger
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from .shared import abort_if_obj_not_found, OneObjCrudResource, ManyObjCrudResource
from ..container import AppContainer
from ..db.base import Database
from ..db.models import UserModel, OrganizationModel, TariffModel


class UserResource(OneObjCrudResource):
    model = UserModel
    returnable_fields = ()
    returnable_name = 'user'
    required_post_fields = (
        'first_name', 'last_name', 'middle_name', 'organization_id', 'status', 'job_title', 'login', 'password', 'role')
    unrequired_post_fields = ()

    def post(self):
        args = self.p.parse_args()
        session: Session
        ps = args.pop('password')
        args['hash_password'] = generate_password_hash(ps)
        logger.info(args)
        with self.db.session() as session:
            obj = self.model(**args)
            session.add(obj)
        return jsonify({'success': 'ok'})


class UsersResource(ManyObjCrudResource):
    model = UserModel
    returnable_fields = (
        '-access_tests.access_users', 'first_name', 'last_name', 'middle_name', 'organization_id', 'status',
        'job_title',
        'login', 'role', 'token', 'organization',)
    returnable_name = 'user'
    rules = ()
