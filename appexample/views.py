from django.shortcuts import render

from common.views import (
    ObjectView,
    NameSearchView,
    VueView
)
from .forms import (
    UserForm
)
from .models import (
    User
)

class Index(VueView):
    pass

class UserEditView(ObjectView): 
    vue_page = 'user_edit.js'
    model = User
    form_class = UserForm
    url = '/appexample/user'
    page = 'edit'

class UserSearchView(NameSearchView):
    properties=['id', 'name', 'brand', 'price', 'group']
    model = User
