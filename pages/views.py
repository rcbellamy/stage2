from django.shortcuts import render

def home( request ):
    graph = user.get_offline_graph( )
    return render( request, 'home.html', {'fm': graph.get( 'me' ) } )