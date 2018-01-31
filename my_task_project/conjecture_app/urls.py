from django.conf.urls import url
from . import views
from conjecture_app.forms import Collatz_Form

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^collatz$',views.form_page_view,name='form_name_view'),
     url(r'^collatz/output$',views.output_view,name='output_view'),
    

]
