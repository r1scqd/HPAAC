from .shared import ManyObjCrudResource
from ..db.models import TestSessionModel
from ..resources.shared import OneObjCrudResource


class TestSessionResource(OneObjCrudResource):
    model = TestSessionModel
    returnable_fields = ('user_id', 'date', 'result', 'vr_id', 'test_id', 'test_type')
    returnable_name = "tariff"
    required_post_fields = ('user_id', 'result', 'test_type', 'vr', 'test')
    unrequired_post_fields = ('test_id', 'vr_id')


class TestsSessionResource(ManyObjCrudResource):
    model = TestSessionModel
    returnable_fields = ()
    returnable_name = "tariffs"
