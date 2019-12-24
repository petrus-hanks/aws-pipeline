from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
urlpatterns = [
	path('WhiteListInfo', views.WhiteListInfo.as_view()),
	# path('company/<int:pk>', views.CompanyDetail.as_view()),
	path('CreditInfo', views.CreditInfo.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)