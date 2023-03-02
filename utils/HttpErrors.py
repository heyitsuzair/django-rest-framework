from django.http import HttpResponseNotFound
from rest_framework.renderers import JSONRenderer


def HttpNotFound(message):
    return HttpResponseNotFound(JSONRenderer().render({"msg": message}))
