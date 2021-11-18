from django import forms


class CategoryFieldForm(forms.ModelForm):

    class Media:
        js = ('category.js',)

