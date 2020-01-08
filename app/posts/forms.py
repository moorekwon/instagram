from django import forms


class PostCreateForm(forms.Form):
    """
    이 Form에 들어갈 입력 요소
    Image(File)
    Text
    """
    text = forms.CharField(label="text", max_length=200)
    # image = forms.ImageField(label="image")
    image = forms.FileField(widget=forms.ClearableFileInput(
        attrs={
            'multiple': True
        }))
