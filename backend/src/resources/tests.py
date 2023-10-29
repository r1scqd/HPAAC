from .shared import ManyObjCrudResource
from ..db.models import TestModel, VRModel
from ..resources.shared import OneObjCrudResource


class TestResource(OneObjCrudResource):
    model = TestModel
    returnable_fields = ('name', 'text')
    returnable_name = "test"
    required_post_fields = ('name', 'text')


class TestsResource(ManyObjCrudResource):
    model = TestModel
    returnable_fields = ('name', 'text')
    returnable_name = "tests"


class VrResource(OneObjCrudResource):
    model = VRModel
    returnable_fields = ()
    returnable_name = "vr"
    required_post_fields = ('name', 'link')


class VrsResource(ManyObjCrudResource):
    model = VRModel
    returnable_fields = ()
    returnable_name = "vrs"
