from rest_framework import generics, mixins
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from users import decorator
from .models import Product
from .forms import RegisterForm
from .serializers import ProductSerializers
from django.views.generic.edit import FormView




@method_decorator(decorator.admin_required, name= 'dispatch')
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            stock = form.data.get('stock'),
            description = form.data.get('description')
        )
        product.save()
        return super().form_valid(form)

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

class ProductListApi(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializers
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailApi(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = Product
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)