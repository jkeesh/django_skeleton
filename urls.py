from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	(r'^$', 'todo.views.index'),
	(r'^register$', 'todo.views.register'),
	(r'^login/?$', "todo.views.login"),
    (r'^logout/?$', "todo.views.logout"),


    # Example:
    # (r'^contacts/', include('contacts.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)
