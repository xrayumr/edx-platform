"""Admin interface for the util app. """


from django.contrib import admin

from util.models import LoginRateLimitConfiguration, RateLimitConfiguration

admin.site.register(LoginRateLimitConfiguration)
admin.site.register(RateLimitConfiguration)
