from django.urls import path
from .views import *

urlpatterns = [
    path('json/<str:date>', ret_json_date, name = "json_with_date"),
    path('xlsx/<str:date>', ret_xlsx_date, name = "xlsx_with_date"),
    path('json/', ret_json),
    path('xlsx/', ret_xlsx),
]
