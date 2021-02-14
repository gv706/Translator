from django.urls import path
from LangTranslator import views

urlpatterns=[
  path('',views.index,name="index"),
]