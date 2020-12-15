from captcha.fields import CaptchaField
from django import forms


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class CommentForm(forms.Form):
    captcha = CaptchaField()
    author = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=500)
