from .shared import ManyObjCrudResource
from ..db.models import OrganizationModel
from ..resources.shared import OneObjCrudResource


class OrganizationResource(OneObjCrudResource):
    model = OrganizationModel
    returnable_fields = ()
    returnable_name = "tariff"
    required_post_fields = ('phone', 'email', 'ITN', 'name', 'address', 'tariff_id')


class OrganizationsResource(ManyObjCrudResource):
    model = OrganizationModel
    returnable_fields = ()
    returnable_name = "tariffs"
