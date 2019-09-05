from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView

# def index_view(request):
#     # return HttpResponse('<h1>Hello world!</h1>')
#     return render(request, 'notebook_shop/index.html')


# class IndexPageView(View):
#     template_name = 'notebook_shop/index.html'
#
#     def get(self, request):
#
#         args = {'spam': 'eggs'}
#         return render(request, self.template_name, context=args)

class IndexPageView(TemplateView):
    template_name = 'notebook_shop/index.html'


class CatalogPageView(TemplateView):
    template_name = 'notebook_shop/catalog.html'


class ContactsPageView(TemplateView):
    template_name = 'notebook_shop/contacts.html'


class MiAirPageView(TemplateView):
    template_name = 'notebook_shop/content/mi_air.html'


class LenovoPageView(TemplateView):
    template_name = 'notebook_shop/content/lenovo_330.html'
