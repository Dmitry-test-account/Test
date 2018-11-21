#from MyWebPage.models import Mark
from MyWebPage.models import BrandType
from django.conf import settings


#def trade_marks(request):
#    return {'trade_marks': Mark.objects.all()}



def brand_types(request):
    return {'brand_types': BrandType.objects.all()}


def stripe_pk_key(request):
    return {'stripe_pk_key': settings.STRIPE_PUBLIC_KEY}
