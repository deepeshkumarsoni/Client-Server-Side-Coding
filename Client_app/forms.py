from django import forms

class Student_Form(forms.Form):

    S_Name = forms.CharField(
        label='Enter Your Name :',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Name'
            }
        )
    )
    S_Rollno = forms.IntegerField(
        label = 'Enter Your RollNo :',
        widget = forms.NumberInput(
           attrs={
               'class' : 'form-control',
               'placeholder' : 'Your RollNo'
           }
        )
    )
    S_Class = forms.IntegerField(
        label = 'Enter Your Class :',
        widget = forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Class'
            }
        )
    )
    S_Location = forms.CharField(
        label = 'Enter Your Location :',
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Location'
            }
        )
    )