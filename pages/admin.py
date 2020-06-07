from django.contrib import admin
from . models import News, Project, Service,Contact,Media

admin.site.register(News)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Media)