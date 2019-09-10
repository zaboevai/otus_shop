
from django.views.generic import TemplateView

from .models import Goods


class IndexPageView(TemplateView):
    template_name = 'notebook_shop/index.html'


class CatalogPageView(TemplateView):
    template_name = 'notebook_shop/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goods_list = Goods.objects.all()
        data = []
        for goods in goods_list:
            goods = {'id': goods.id, 'name': goods.name, 'url': goods.image.url}
            data.append({'laptop': goods})

        context.update({'goods':data})

        return context


class ContactsPageView(TemplateView):
    template_name = 'notebook_shop/contacts.html'


class GoodInfoView(TemplateView):
    template_name = 'notebook_shop/good.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.GET['id']
        goods = Goods.objects.get(id=id)
        good_info = {'id': goods.id, 'name': goods.name, 'descr':goods.description, 'url': goods.image.url}
        context.update(good_info)

        return context