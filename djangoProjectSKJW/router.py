from zolnierze.api.viewsets import *
from zolnierze.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Zolnierze', ZolnierzViewSet)
router.register('Kontrakty', KontraktyViewSet)
router.register('Przepustki', PrzepustkiViewSet)
router.register('Wnioski', WnioskiViewSet)