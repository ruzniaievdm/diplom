from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.Enterprise.forms import EnterpriseForm
from core.Enterprise.models import Enterprise


def enterprise_list(request):
    enterprises = Enterprise.objects.all().order_by('id')

    return render(request, 'Enterprise/enterprise_list.html',
                  {'enterprises': enterprises})


def enterprise_detail(request, enterprise_id):
    enterprise = get_object_or_404(Enterprise, pk=enterprise_id)
    return render(request, 'Enterprise/enterprise_detail.html',
                  {'enterprise': enterprise})


def enterprise_add(request):
    if request.method == "POST":
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            enterprise = form.save(commit=False)
            enterprise.name = form.cleaned_data['name']
            enterprise.save()
            return redirect('enterprise-list')
    else:
        form = EnterpriseForm()
    return render(request, 'Enterprise/enterprise_add.html',
                  {'form': form})


def enterprise_edit(request, enterprise_id):
    enterprise = get_object_or_404(Enterprise, pk=enterprise_id)
    if request.method == "POST":
        form = EnterpriseForm(request.POST, instance=enterprise)
        if form.is_valid():
            enterprise = form.save(commit=False)
            enterprise.name = form.cleaned_data['name']
            enterprise.save()
            return redirect('enterprise-list')
    else:
        form = EnterpriseForm(instance=enterprise)
    return render(request, 'Enterprise/enterprise_edit.html',
                  {'form': form})


def enterprise_delete(request, enterprise_id):
    enterprise = get_object_or_404(Enterprise, pk=enterprise_id)

    try:
        enterprise.delete()
    except ProtectedError:
        messages.warning(request, _('Enterprise has related objects and can not be deleted'))

    return redirect('enterprise-list')
