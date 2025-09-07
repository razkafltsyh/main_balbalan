from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496340',
        'name': 'Muhammad Razka Faltasyah',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
