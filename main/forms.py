from django import forms


class MainForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    number = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    agree = forms.BooleanField(widget=forms.CheckboxInput, required=True)


class MainFormMob(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    number = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    agree = forms.BooleanField(widget=forms.CheckboxInput, required=True)

    def __init__(self, *args, **kwargs):
        super(MainFormMob, self).__init__(*args, **kwargs)
        self.fields['agree'].widget.attrs['class'] = 'agree_mob'


class HelpForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    number = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    need = forms.CharField(max_length=200, required=True)
    agree = forms.BooleanField(widget=forms.CheckboxInput, required=True)

    def __init__(self, *args, **kwargs):
        super(HelpForm, self).__init__(*args, **kwargs)
        self.fields['agree'].widget.attrs['class'] = 'agree_help'


class HelpYouForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    number = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    need = forms.CharField(max_length=200, required=True)
    agree = forms.BooleanField(widget=forms.CheckboxInput, required=True)

    def __init__(self, *args, **kwargs):
        super(HelpYouForm, self).__init__(*args, **kwargs)
        self.fields['agree'].widget.attrs['class'] = 'agree_help_you'


class CanToHelpForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    number = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(required=True)
    help = forms.CharField(max_length=200, required=True)
    agree = forms.BooleanField(widget=forms.CheckboxInput, required=True)

    def __init__(self, *args, **kwargs):
        super(CanToHelpForm, self).__init__(*args, **kwargs)
        self.fields['agree'].widget.attrs['class'] = 'agree_can_help'
