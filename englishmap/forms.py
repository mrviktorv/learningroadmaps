from django import forms
from .models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['nameR', 'bodyR' 
        # 'comment'
        ]
    
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['nameR'].required = True