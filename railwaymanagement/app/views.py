from django.shortcuts import render

_HOME_PAGE = 'index.html'


def index(req):
    return render(req, _HOME_PAGE)
