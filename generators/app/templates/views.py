from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

# import json
# from .models import __all__
# from .serializers import __all__

def initialData( user ):
    ''' this is used to get the full application data on page load '''
    return {
        "user": { "name": user.username, "id": user.pk },
    }

class IndexView( TemplateView ):
    template_name="index.html"

    def get_context_data( self, **kwargs ):
        ctx=TemplateView.get_context_data( self, **kwargs )
        ctx.update({
        })
        return ctx

class UserHomeView( DetailView ):
    slug_field="username"
    slug_url_kwarg="username"
    template_name="user.html"
    model=User

    @method_decorator( login_required )
    def dispatch( self, request, *args, **kwargs ):
        if request.is_ajax():
            ''' a request for initial data from a javscript application'''
            data=initialData( request.user )
            return JsonResponse( data )
        return DetailView.dispatch( self, request, *args, **kwargs )

    def get_context_data( self, *args, **kwargs ):
        ctx=super( UserHomeView, self ).get_context_data( *args, **kwargs )
        ctx.update({
        })
        return ctx
