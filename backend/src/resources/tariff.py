from .shared import ManyObjCrudResource
from ..db.models import TariffModel
from ..resources.shared import OneObjCrudResource


class TariffResource(OneObjCrudResource):
    model = TariffModel
    returnable_fields = ()
    returnable_name = "tariff"
    required_post_fields = ('name', 'price', 'description')


class TariffsResource(ManyObjCrudResource):
    model = TariffModel
    returnable_fields = ()
    returnable_name = "tariffs"
