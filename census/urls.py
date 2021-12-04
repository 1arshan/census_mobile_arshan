from django.urls import path
from django.urls.resolvers import URLPattern
from .views import StateView,DistrictView,ChildView,Logout,ChildGetView,StateGetView,DistrictGetView,FileView

urlpatterns =[
    path("master/get-state/", StateGetView.as_view(), name='state_get'),
    path("state/create", StateView.as_view(), name='state_post'),
    path("master/get-district/", DistrictGetView.as_view(), name='district_get'),
    path("district/create/", DistrictView.as_view(), name='district_post'),
    path("beneficiary/child-profile-create", ChildView.as_view(), name='child_post'),
    path("beneficiary/get-child-profile", ChildGetView.as_view(), name='child_get'),
    path('user/logout',Logout.as_view()),
    path("upload-image/s3-upload", FileView.as_view(), name='file_get'),
]


