from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(request, self):
        return render(request, 'spotapp/templates/base.html')