from django.conf.urls import patterns, include, url
from admin.views import user
from admin.views import role
from admin.views import userList
from admin.views import roleList
from admin.views import addRoleForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'localhostCMS.views.home', name='home'),
    #url(r'^localhostCMS/', include('localhostCMS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^adminself/', include(admin.site.urls)),
     url(r'^user/$',user),
     url(r'^role/$',role),
     url(r'^userList/$',userList),
     url(r'^roleList/$',roleList),
     url(r'^addRoleForm/$',addRoleForm),
)
