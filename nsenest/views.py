from django.shortcuts import render
from django.views.generic import base


class Index(base.View):
    def get(self, request):
        return render(request, template_name='index.html')
