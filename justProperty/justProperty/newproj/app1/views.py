from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import tblProperty
# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def viewAll(request):
    propertyList = tblProperty.objects.all()

    return render(request, 'viewAll.html', {'propertyList':propertyList})


def addNewProperty(request):
    success= False
    
    if request.method == "GET":
        form = PropertyForm()
    else:
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    return render(request, 'addNewProperty.html', {'success':success, 'form':form})

def editProperty(request, property_id):
    property = tblProperty.objects.get(pk=property_id)
    form = PropertyForm(request.POST or None, instance=property)

    if form.is_valid():
        form.save() 
        return redirect('viewAll')

    return render(request, 'editProperty.html', {"property": property, "form":form})

def deleteProperty(request, property_id):
    property = tblProperty.objects.get(pk=property_id)
    property.delete()

    return redirect('viewAll')