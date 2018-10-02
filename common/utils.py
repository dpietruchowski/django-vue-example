import appexample.models
from django import forms

from decimal import *

def get_all_fields(instance):
    fields = list(instance().base_fields)
    for field in list(instance().declared_fields):
        if field not in fields:
            fields.append(field)
    return fields

def form_serializer(instance, form_class):
    return field_serializer(instance, get_all_fields(form_class))

def field_serializer(instance, fields):    
    form_array = {}
    for field in fields:
        attr = getattr(instance, field)
        if isinstance(attr, str):
            pass
        elif isinstance(attr, int):
            attr = int(attr)
        elif isinstance(attr, Decimal):
            attr = float(attr)
        elif isinstance(attr, appexample.models.User):
            if attr is None:
                attr = -1
            else:
                attr = attr.pk
        elif attr is None:
            attr = ""
        else:
            raise Exception('Unknown {} field type'.format(field))
        form_array.update({field: attr})
    return form_array

def print_tree(root_pk, tree_data, level):
    print('  ' * level + str(tree_data[root_pk]['fields']))
    children = tree_data[root_pk]['children']
    for child_pk in children:
        print_tree(child_pk, tree_data, level+1)