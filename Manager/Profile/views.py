from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from Manager.Profile.forms import FamilyMemberFormSet
from core.Profile.models import Profile


class ProfileList(ListView):
    model = Profile


class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    form_class = Profile
    template_name = 'Profile/profile_form.html'
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()
            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)


class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
