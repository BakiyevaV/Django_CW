from django import forms
from .models import Bb
from .models import Bb, Comments, Rubric


# BbForm = modelform_factory(Bb, fields=('title', 'content', 'price', 'rubric', 'feature'),
#                            labels={'title':'Название товара'},
#                            help_texts={'rubric':'Выбери рубрику'},
#                            field_classes={'price': DecimalField},
#                            widgets={'rubric':Select(attrs={'size': 8})})
# для отображения всех форм __all__


from django import forms
from .models import Bb

class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'feature')
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Выбери рубрику'}
        field_classes = {'price': forms.DecimalField}
        widgets = {'rubric': forms.Select(attrs={'size': 8})}
    # class Meta:
    #     model = Bb
    #     fields = ('title', 'content', 'price', 'rubric', 'feature')
    #     labels = {'title': 'Название товара'}
    #     help_text={'rubric':'Выбери рубрику'}
    #     field_classes={'price': DecimalField}
    #     widgets={'rubric':Select(attrs={'size': 8}


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_creator', 'comment')
