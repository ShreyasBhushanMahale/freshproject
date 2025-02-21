from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Your FULL name", max_length=100, required=True)
    age = forms.IntegerField(label="Your age in years", required=True)
    email = forms.EmailField(label="Your email address", max_length=100, required=True)
    message = forms.CharField(
        label="Your message/opinion/What do you feel about this",
        widget=forms.Textarea,
        required=False,
    )
