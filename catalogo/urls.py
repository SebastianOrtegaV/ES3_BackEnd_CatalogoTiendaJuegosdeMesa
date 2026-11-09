from django.urlsimportpath
from .importviews
urlpatterns = [
path("",views.inicio,name="catalogo_inicio"),
path("ofertas/",views.ofertas, name="catalogo_ofertas"),