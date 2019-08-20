from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Student_Data
from Client_app import forms

def Student_View(request):
    if request.method == 'POST':
        sform = (request.POST)
        if sform.is_valid():
            name = request.POST.get('S_Name')
            rollno = request.POST.get('S_Rollno')
            sclass = request.POST.get('S_Class')
            location = request.POST.get('S_Location')

            data = Student_Data(
                S_Name = name,
                S_Roll = rollno,
                S_Class = sclass,
                S_Location = location
            )
            data.save()
            sform = Student_Form()
            return render(request,'abc.html',{'sform':sform})
    else:
        sform = Student_Form()
        return render(request,'abc.html',{'sform':sform})

