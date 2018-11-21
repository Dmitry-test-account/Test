from django.views.generic import TemplateView, ListView, FormView
from MyWebPage.forms import RegisterForm
from MyWebPage.models import Products, BrandType
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.urls import reverse
from django.views import View




class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        products = Products.objects.all()[:100]
        context['products'] = products
        return context


class BrandView(ListView):
    template_name = 'brand_type.html'
    model = Products

    def get_queryset(self):
        brand_type = get_object_or_404(BrandType, id=self.kwargs['brand_type_id'])
        queryset = self.model.objects.filter(brand_type=brand_type)
        return queryset


class Register(FormView):
    template_name = 'auth/registration.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)


class CheckoutView(View):
    def post(self, request, *args, **kwargs):
        import stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        product = Products.objects.get(id=kwargs['product_id'])
        stripe.Charge.create(
            amount=int(product.price_for_stripe),
            currency="usd",
            source=request.POST['stripeToken'],  # obtained with Stripe.js
            description=""
        )
        product.count -= 1
        product.save()
        return redirect(reverse('buy'))


class BuyView(TemplateView):
    template_name = 'buy.html'
