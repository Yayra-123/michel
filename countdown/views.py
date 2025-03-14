from django.shortcuts import render
from datetime import datetime

def index(request):
    # Date cible (le 24 du mois en cours)
    today = datetime.now()
    target_date = datetime(today.year, today.month, 24, 0, 0, 0)

    # Si aujourd'hui est déjà le 24, passer au mois suivant
    if today.day >= 24:
        target_date = datetime(today.year, today.month + 1, 24, 0, 0, 0)
        if target_date.month > 12:
            target_date = datetime(today.year + 1, 1, 24, 0, 0, 0)

    # Calcul du nombre de jours restants
    days_left = (target_date - today).days

    return render(request, 'countdown/index.html', {'days_left': days_left})
