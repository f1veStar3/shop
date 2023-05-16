from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cart , CartItem , Product, Category
from django.core.paginator import Paginator
from django_user_agents.utils import get_user_agent


class BaseMixin(View):

    def dispatch(self, request, *args, **kwargs):
        category_list = Category.objects.filter(is_available=True)

        user_agent = get_user_agent(request)
        if user_agent.is_mobile:
            categories_per_page = 2
        else:
            categories_per_page = 4

        paginator = Paginator(category_list, categories_per_page)

        page = request.GET.get('page')

        categories = paginator.get_page(page)


        self.categories = categories
        return super().dispatch(request, *args, **kwargs)





class CartMixin(LoginRequiredMixin,View):

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        if not cart:
            cart = Cart.objects.create(user=user)
        cart_items = CartItem.objects.filter(cart=cart)

        total = sum(item.price * item.qty for item in cart_items)

        self.total = total
        self.user = user
        self.cart_items = cart_items
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)

