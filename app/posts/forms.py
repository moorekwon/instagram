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

    def save(self):
        pass


class CommentCreateForm(forms.Form):
    comment = forms.CharField(max_length=50, widget=forms.Textarea())

    def save(self, post, author):
        post.postcomment_set.create(author=author, content=self.cleaned_data['comment'])
