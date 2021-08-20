from .models import *

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Submit, Layout, ButtonHolder

class incomeForm(forms.ModelForm):

    class Meta:

        model = Income
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Fieldset(
                    'personName',
                    'enteredAmount',
                )
            )

class expenseForm(forms.ModelForm):

    class Meta:

        model = Expense
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Fieldset(
                    'personName',
                    'category',
                    'expenseAmount',
                ),
                ButtonHolder(
                    Submit('submit', 'Submit', css_class='button green')
                )
            )
