from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import formset_factory, BaseFormSet

from core.Department.models import Department
from core.Enterprise.models import Enterprise


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    name = forms.CharField(
        max_length=64, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Department name'),
                   'class': 'form-control', 'type': 'text', }))

    enterprise = forms.ModelChoiceField(queryset=Enterprise.objects.all(), empty_label=None,
                                        label='Предприятие', widget=forms.Select(
            attrs={'id': 'enterprise', 'class': 'form-control'}), )

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Department.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Department with name %(name)s already exists'), params={'name': name},
                                        code='invalid')
        # raise forms.ValidationError(self.error_messages['password_mismatch'])
        return name

        # error_messages = {
        #     'password_mismatch': _("The two password fields didn't match."),
        # }


# class BaseDepartmentFormSet(BaseFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
#         names = []
#         for form in self.forms:
#             name = form.cleaned_data['name']
#             if name in names:
#                 raise forms.ValidationError('In a set must have distinct names.')
#             names.append(name)
#
#
# DepartmentFormSet = formset_factory(DepartmentForm, formset=BaseDepartmentFormSet, can_delete=True, extra=1)
