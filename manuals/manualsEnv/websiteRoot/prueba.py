from pages.models import Page
pg = Page.objects.get(permalink='/')
print(pg.title)
