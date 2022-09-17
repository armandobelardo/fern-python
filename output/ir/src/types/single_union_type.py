from types.single_union_type_properties import SingleUnionTypeProperties
from types.type_reference import TypeReference

import pydantic
from commons.wire_string_with_all_casings import WireStringWithAllCasings
from commons.with_docs import WithDocs


class SingleUnionType(WithDocs):

    discriminant_value: WireStringWithAllCasings = pydantic.Field(alias="discriminantValue")
    value_type: TypeReference = pydantic.Field(alias="valueType")
    shape: SingleUnionTypeProperties

    class Config:

        allow_population_by_field_name = True
