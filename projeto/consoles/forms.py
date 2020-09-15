from django import forms
from .models import Console

class ConsoleForm(forms.ModelForm):
    class Meta:
        model = Console
        fields = '__all__'

    def clean_lancamento(self):
        lancamento = self.cleaned_data['lancamento']
        if int(lancamento) < 1972 or int(lancamento) > 2020:
            raise forms.ValidationError('Nenhum console foi lançado nesse ano!')
        return lancamento