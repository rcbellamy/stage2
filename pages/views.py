from django.shortcuts import render

def home( request ):
    try:
        graph = user.get_offline_graph( )
        fm = graph.get( 'me' )
    except:
        fm = ''
    return render( request, 'home.html', {'fm': fm } )