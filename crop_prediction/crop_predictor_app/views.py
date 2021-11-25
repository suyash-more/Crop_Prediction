# Inbuilt Imports
from django.shortcuts import render
import numpy as np
import warnings
import pickle

# Custom Imports
from .forms import CropDetailsForm
from .models import CropDetails

# ignore warnings
warnings.filterwarnings('ignore')

def crop_detail_view(request):
    if request.method == 'POST':
        result_str = "No Crop Suitable for the Given Values"
        data = request.POST
        name = data["name"]
        nitrogen_content = data["nitrogen_content"]
        phosphorus_content = data["phosphorus_content"]
        potassium_content = data["potassium_content"]
        temperature = data["temperature"]
        humidity = data["humidity"]
        ph = data["ph"]
        rainfall = data["rainfall"]
        form = CropDetailsForm(request.POST)
        if form.is_valid():
            crop_model=pickle.load(open("C:\\Users\\hp\\Desktop\\pem keys\\Crop_Prediction\\crop_prediction\\crop_predictor_app\\model\\kmeans_model.sav", 'rb'))
            prediction = crop_model.predict((np.array([[nitrogen_content, phosphorus_content, potassium_content, temperature, humidity, ph, rainfall]])))
            crop = CropDetails(name=name, nitrogen_content=nitrogen_content, phosphorus_content=phosphorus_content, potassium_content=potassium_content, temperature=temperature
            , humidity=humidity, ph=ph, rainfall=rainfall)
            crop.save()
            if bool(prediction):
                result_str = "No Crop Suitable for the Given Values"
            else :
                result_str = "Crops which can be planted are : "
                for crop in prediction:
                    result_str += str(crop)
            return render(request, 'result-page.html', {"crop":result_str})
    else:
        form = CropDetailsForm()

    return render(request, 'home-page.html', {'form': form})
    

def resultpage(request):
    return render(request, 'result-page.html')