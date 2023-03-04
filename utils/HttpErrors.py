from django.http import HttpResponseNotFound, HttpResponse, HttpResponseBadRequest
from rest_framework.renderers import JSONRenderer


def HttpNotFound(message):
    return HttpResponseNotFound(JSONRenderer().render({"msg": message}))


def HttpOK(message):
    return HttpResponse(JSONRenderer().render({"msg": message}))


def HttpBadRequest(message):
    return HttpResponseBadRequest(JSONRenderer().render({"msg": message}))
