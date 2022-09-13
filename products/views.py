from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm
# Create your views here.

class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context

class CommentCreateView(generic.CreateView, SuccessMessageMixin):
    model = Comment
    form_class = CommentForm
    success_message = "%(calculated_field)s was created successfully"

    # def get_success_url(self):
    #     return reverse('product_list')
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        # messages.success(self.request, "comment add sucesfuly")

        return super().form_valid(form)