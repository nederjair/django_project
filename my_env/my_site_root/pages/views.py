from django.shortcuts import render
from pathlib import Path
from .models import PageModel
# Create your views here.
def index(request, pagename):
    pagename = '/' + pagename
    pg = PageModel.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.body_text,
        'last_updated': pg.update_date,
        'page_list': PageModel.objects.all(),
    }
    return render(request, Path('pages', 'page.html'), context)