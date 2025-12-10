# resume_app/forms.py
from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email','education', 'phone', 'skills', 'experience','acknowledgment', 'hobbies']
        widgets = {
            'experience': forms.Textarea(attrs={'rows':2}),
            'education': forms.Textarea(attrs={'rows':4}),
        
            'skills': forms.Textarea(attrs={'rows':2}),
            'acknowledgment': forms.Textarea(attrs={'rows':2}),
            'hobbies': forms.Textarea(attrs={'rows':2}),
            'languages': forms.Textarea(attrs={'rows':2}),
            
        }
