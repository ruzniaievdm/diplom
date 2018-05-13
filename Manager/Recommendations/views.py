from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.Recommendations.forms import RecommendationsForm
from core.Recommendations.models import Recommendations


def recommendations_list(request):
    recommendations = Recommendations.objects.all().order_by('id')
    return render(request, 'Recommendations/recommendations_list.html',
                  {'recommendations': recommendations})


def recommendations_add(request):
    if request.method == "POST":
        form = RecommendationsForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.unique = form.cleaned_data['unique']
            recommendation.work = form.cleaned_data['work']
            recommendation.recommend_cost = form.cleaned_data['recommend_cost']
            recommendation.recommend_duration = form.cleaned_data['recommend_duration']
            recommendation.relative_duration = form.cleaned_data['relative_duration']
            recommendation.relative_cost = form.cleaned_data['relative_cost']
            recommendation.relative_importance = form.cleaned_data['relative_importance']
            recommendation.save()
            return redirect('recommendations-list')
    else:
        form = RecommendationsForm()
    return render(request, 'Recommendations/recommendations_add.html',
                  {'form': form, })


def recommendations_delete(request, recommendations_id):
    recommendation = get_object_or_404(Recommendations, pk=recommendations_id)
    try:
        recommendation.delete()
    except ProtectedError:
        messages.warning(request, _('Recommendation has related objects and can not be deleted'))
    return redirect('recommendations-list')
