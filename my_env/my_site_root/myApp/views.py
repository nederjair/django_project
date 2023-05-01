from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AppForm
from pages.models import PageModel

# Create your views here.
def app_req(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            #form.save()
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            summa = num1 + num2
            return render(request, 'myApp/submitted.html',
                            {'page_list': PageModel.objects.all(), 
                             'num1': num1, 'num2': num2 ,'result': summa}) 
    else:
        form = AppForm()
        if 'summited' in request.GET:
            return render(request, 'myApp/submitted.html',
                            {'page_list': PageModel.objects.all()})

    return render(request, 'myApp/app.html',
            {'form': form, 'page_list': PageModel.objects.all()})