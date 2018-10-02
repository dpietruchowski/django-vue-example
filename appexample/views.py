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

class IndexView(VueView):
    pass

class UserListView(VueView):
    vue_page = 'user_list.js'

class UserEditView(ObjectView): 
    vue_page = 'user_edit.js'
    model = User
    form_class = UserForm
    url = '/appexample/user'
    page = 'edit'

class UserSearchView(NameSearchView):
    properties=['id', 'name', 'surname', 'age']
    model = User
