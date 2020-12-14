from captcha.fields import CaptchaField
from django import forms


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class CommentForm(forms.Form):
    captcha = CaptchaField()
    author = forms.CharField(label='Username', max_length=100)
    comment = forms.CharField(label='Comment', max_length=500)
