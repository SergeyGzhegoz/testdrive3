from django.shortcuts import render, redirect
from .models import Drive, Car
from .forms import DriveForm
from .filters import PostFilter


def index(request):
    tasks_all = Drive.objects.order_by('id')
    tasks = PostFilter(request.GET, queryset=tasks_all)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def Testdrive(request):
    error = ""
    if request.method == 'POST':
        form = DriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    # cars_all = Car.objects.order_by('id')
    # cars_list = []
    # for el in cars_all:
    #     cars_list.append((f'{el.marka} {el.model}', f'{el.marka} {el.model}'))
    form = DriveForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/Testdrive.html', context)
