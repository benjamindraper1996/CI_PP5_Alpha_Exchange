"""
A module containing the views within the home app.
"""
from django.shortcuts import render


def index(request):
    """ Displays the home page """
    return render(request, 'home/index.html')
