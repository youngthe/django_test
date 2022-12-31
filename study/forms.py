from django import forms

class AccountForm(forms.Form):
    account = forms.CharField(label='Your name', max_length=15)
    password = forms.CharField(label='Your password', max_length=20)

    def __str__(self):
        return self.account