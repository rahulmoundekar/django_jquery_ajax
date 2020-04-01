from django import forms

from facebook_comment_box.models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(max_length=45,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Message'}))

    class Meta:
        model = Message
        fields = "__all__"
