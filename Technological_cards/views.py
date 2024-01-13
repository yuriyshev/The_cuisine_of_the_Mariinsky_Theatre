from django.shortcuts import render


def index(request):
    return render(request, 'Technological_cards/index.html')