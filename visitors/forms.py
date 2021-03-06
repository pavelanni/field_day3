from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Visitor


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ('first_name',
                  'last_name',
                  'call_sign',
                  'nfarl_member',
                  'contact_me',
                  'email',
                  'first_time',
                  'younger_than_18',
                  )
        labels = {
            'nfarl_member': _('NFARL Member'),
        }

        help_texts = {
            'nfarl_member': _('Are you a member of NFARL?'),
        }

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))
