from django import forms

# Create your forms here.

class BabyNameForm(forms.Form):
    name = forms.CharField(max_length=12, required=True)
    sex = forms.ChoiceField(choices=[('boy', 'boy'), ('girl', 'girl')], 
                            required=True)

