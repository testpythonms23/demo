from .models import Branch

def menu_links(request):
    links = Branch.objects.all()
    return dict(links=links)