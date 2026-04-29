from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from .models import CartItem, Cart
from products.models import Product
from django.urls import reverse_lazy
from django.views.generic import DeleteView


# ✅ 1. Ajouter au panier
class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        try:
            quantity = int(request.POST.get('quantity'))
            if quantity < 1:
                quantity = 1
        except:
            quantity = 1

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            if not request.session.session_key:
                request.session.create()
            cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        cart_item.save()

        return redirect('cart_detail')


# ✅ 2. Page panier (DOIT ÊTRE EN DEHORS)
class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart/detail_cart.html'
    context_object_name = 'cart'

    def get_object(self):
        if self.request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=self.request.user)
        else:
            if not self.request.session.session_key:
                self.request.session.create()
            cart, _ = Cart.objects.get_or_create(session_key=self.request.session.session_key)

        return cart
    


# ✅ 3. Supprimer un article du panier
class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'cart/cartitem_delete.html'
    success_url = reverse_lazy('cart_detail')
    context_object_name = 'cartitem'

    # fct prédéfini dans class-based-views détermine quels objets cartitem à supprimer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            print(self.request.user)
            cart = get_object_or_404(Cart, user=self.request.user)
        else:
            session_key = self.request.session.session_key
            if not session_key:
                # S'il n'y en a pas (nouvelle session) → on retourne un queryset vide.
                return CartItem.objects.none()
            cart = get_object_or_404(Cart, session_key=session_key)

        return CartItem.objects.filter(cart=cart)
