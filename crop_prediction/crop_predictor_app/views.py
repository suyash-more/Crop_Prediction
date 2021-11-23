from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CropDetailsForm
from .model.crop_prediction_model import give_prediction

# Create your views here.
def index(request):
    # return render
    return HttpResponse("suyash is here")

def crop_detail_view(request):
    if request.method == 'POST':
        form = CropDetailsForm(request.POST)
        if form.is_valid():
            return render(request, 'result-page.html', {'crop': give_prediction()})
    else:
        form = CropDetailsForm()

    return render(request, 'home-page.html', {'form': form})

def resultpage(request):
    return render(request, 'result-page.html')
    