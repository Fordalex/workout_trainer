from django.shortcuts import render

# Create your views here.
def workout_menu(request):
    return render(request, 'workout/workout_menu.html')