from django.contrib import admin

# Register your models here.
from .models import user, LoginUser, SignupUser
admin.site.register(user)

from .models import FormModel
admin.site.register(FormModel)
admin.site.register(LoginUser)
admin.site.register(SignupUser)