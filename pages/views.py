from django.shortcuts import render
from django_facebook.api import get_facebook_graph

def home( request ):
    try:
        #graph = user.get_offline_graph( )
        graph = get_facebook_graph( request )
        fm = graph.get( 'me' )
    except:
        fm = ''
    return render( request, 'home.html', {'fm': fm } )