from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
                'style': 'width: 100%; padding: 0.8rem 1rem; border: 1px solid #cbd5e1; border-radius: 8px; font-family: inherit; font-size: 0.95rem;'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'name@example.com',
                'style': 'width: 100%; padding: 0.8rem 1rem; border: 1px solid #cbd5e1; border-radius: 8px; font-family: inherit; font-size: 0.95rem;'
            }),
            'subject': forms.Select(choices=[
                ('General Inquiry', 'General Inquiry'),
                ('Player Tryouts / Joining', 'Player Tryouts / Joining'),
                ('Sponsorship & Partnerships', 'Sponsorship & Partnerships'),
                ('Media & Press', 'Media & Press')
            ], attrs={
                'style': 'width: 100%; padding: 0.8rem 1rem; border: 1px solid #cbd5e1; border-radius: 8px; font-family: inherit; font-size: 0.95rem; background: var(--pure-white);'
            }),
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Type your message here...',
                'style': 'width: 100%; padding: 0.8rem 1rem; border: 1px solid #cbd5e1; border-radius: 8px; font-family: inherit; font-size: 0.95rem; resize: vertical;'
            }),
        }