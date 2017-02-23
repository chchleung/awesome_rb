from django import forms


class BlogForm(forms.Form):
    caption = forms.CharField(label='title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    # CharField 表示字符类型,当你在本地显示这个表单的时，content字段被显示成`` input type=”text”`` ，
    # 而它应该被显示成<`` textarea`` >。我们可以通过设置* widget* 来修改它

class TagForm(forms.Form):
    tag_name = forms.CharField()