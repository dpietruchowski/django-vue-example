from django import forms
from django.middleware import csrf
from django.core import serializers
from django.views.generic.edit import (
    ModelFormMixin, 
    ProcessFormView, 
    SingleObjectTemplateResponseMixin, 
)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView as GenericTemplateView
from django.views.generic import View

from django.http import HttpResponse, JsonResponse

from decimal import *

import json
import pdb

from .utils import *

class VueView(GenericTemplateView):
    vue_page = "index.js"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vue_context'] = {}
        context['vue_page'] = self.vue_page
        self.template_name = 'index.html'
        return context

"""
MUST BE DEFINED IN SUBCLASS:
    template_name
    model
    form_class
    url
    page
    app
"""
class BaseObjectView(ModelFormMixin, ProcessFormView, VueView):
    url = None
    page = None

    def set_object(self):
        if self.kwargs.get(self.pk_url_kwarg, None) is not None:
            self.object = self.get_object()
            self.init_form = [form_serializer(self.object, self.form_class)]
        else:
            self.object = None

    def get(self, request, *args, **kwargs):
        self.set_object()
        self.vue_context = {}
        self.vue_context['csrftoken'] = csrf.get_token(request)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.set_object()
        return super().post(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        response = {'message': 'Usunieto', 'result':True}
        try:
            self.object = self.get_object()
            self.object.delete()
        except:
            response = {'message': 'Nie usunieto', 'result':False}
        return JsonResponse(json.dumps([response]), safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            self.vue_context['pk'] = pk
            self.vue_context['init_form'] = self.init_form
        context['vue_context'] = self.vue_context
        return context

    def get_success_url(self):
        if self.object is not None:
            return self.url + "/edit/" + str(self.object.pk)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'result': 'ok',
                'object': form_serializer(self.object, self.form_class)
            }
            print(data['object'])
            return JsonResponse(data, safe=False)
        else:
            return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {
                'result': 'nok',
                'object': form_serializer(self.object, self.form_class),
                'errors': form.errors
            }
            return JsonResponse(data, safe=False)
        else:
            return response

class ObjectView(SingleObjectTemplateResponseMixin, BaseObjectView):
    template_name_suffix = '_form'


"""
MUST BE DEFINED IN SUBCLASS:
    form_set_class
    related_name
    formset_valid() - custom method for use passed formset
"""
class ObjectSetView(ObjectView):
    form_set_class = None
    extra = 0
    related_name = None

    def formset_factory(self):
        return forms.formset_factory(self.form_set_class, extra=self.extra)
        
    def get_formset_from_request(self):
        FormSet = self.formset_factory()
        return FormSet(self.request.POST)

    def formset_valid(self, formset):
        pass

    def formset_invalid(self, formset):
        errors = []
        for form in formset:
            if not form.is_valid():
                errors.append(form.errors)
        return errors

    def form_valid(self, form):
        if self.object is None:
            return super().form_valid(form)
        formset = self.get_formset_from_request()
        if formset.is_valid():
            Response = super().form_valid(form)
            self.formset_valid(formset)
            return Response
        else:
            self.formset_invalid(formset)
            return super().form_invalid(form)

    def form_invalid(self, form):
        if self.object is not None:
            formset = self.get_formset_from_request()
            if not formset.is_valid():
                self.formset_invalid(formset)
        return super().form_invalid(form)


class QueryView(View):
    queries = []
    properties = []
    def get(self, request, *args, **kwargs):
        avaiable = True
        for query in self.queries:
            if not query in request.GET:
                avaiable = False
                break
        if avaiable:
            return self.search(request)
        return JsonResponse(json.dumps([]), safe=False)

    def json_response(self, model_results):
        results = []
        for obj in model_results:
            results.append(self.convert_object(obj))
        return JsonResponse(json.dumps(results[:10]), safe=False)

    def convert_object(self, obj):
        obj_dict = {}
        for prop in self.properties:
            obj_dict.update({prop: str(getattr(obj, prop))})
        return obj_dict


class NameSearchView(QueryView):
    queries = [u'query']
    model = None
    def search(self, request):
        value = request.GET[u'query']
        model_results = self.model.objects.filter(name__icontains=value)
        return self.json_response(model_results)