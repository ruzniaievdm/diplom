from django.urls import include, path

from Manager.GlossaryArrow import views

urlpatterns = [
    path('list/', views.glossary_arrow_list, name='arrowgloss-list'),
    path('add/', views.glossary_arrow_add, name='arrowgloss-add'),
    path('<int:arrowgloss_id>/edit/', views.glossary_arrow_edit, name='arrowgloss-edit'),
    path('<int:arrowgloss_id>/delete/', views.glossary_arrow_delete, name='arrowgloss-delete'),
]
