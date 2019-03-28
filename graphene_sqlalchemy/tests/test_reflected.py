
from graphene import ObjectType

from ..registry import Registry
from ..types import SQLAlchemyObjectType
from .models import ReflectedEditor

registry = Registry()


class Reflected(SQLAlchemyObjectType):
    class Meta:
        model = ReflectedEditor
        registry = registry


def test_objecttype_registered():
    assert issubclass(Reflected, ObjectType)
    assert Reflected._meta.model == ReflectedEditor
    assert list(Reflected._meta.fields) == ["editor_id", "name"]


class ReflectedWithFieldRenamed(SQLAlchemyObjectType):
    class Meta:
        model = ReflectedEditor
        registry = registry
        rename_fields = {
            "name": "editor_name",
        }


def test_objecttype_registered_with_rename_fields():
    assert list(ReflectedWithFieldRenamed._meta.fields) == ["editor_id", "editor_name"]
