from django.urls import path
from . import views

urlpatterns = [
    	path('',views.domace,name='domace'),
        path('du2_vizitka/',views.du2_vizitka,name='vizitka'),
	]	
