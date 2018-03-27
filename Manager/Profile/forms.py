from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from core.Profile.models import FamilyMember, Profile


class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()


FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
                                            form=FamilyMemberForm, extra=1)
