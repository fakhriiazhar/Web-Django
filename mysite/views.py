from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog

def index(request):
    template_name  = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    print(request.user)

    for k in kategori:
        print(k)

    for a in artikel:
        print(a)

    context = {
        "title": "Welcome to My Site",
        "kategori":kategori,
        "artikel":artikel,
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name  = "landingpage/detail.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect('not_found_artikel')
    
    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)


    context = {
        "title": "Welcome to My Site",
        "artikel":artikel,
        "artikel_lainnya":artikel_lainnya,
    }
    return render(request, template_name, context)

def artikel_not_found(request):
    template_name  = "artikel_not_found.html"
    return render(request, template_name)

def kontak(request):
    template_name  = "kontak.html"
    context = {
        "title": "Welcome to My Site"
    }
    return render(request, template_name, context)

def galeri(request):
    template_name  = "galeri.html"
    context = {
        "title": "Welcome to My Site"
    }
    return render(request, template_name, context)







def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('auth-login')
    template_name  = "dashboard/index.html"
    context = {
        "title": "Welcome to My Site"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name  = "dashboard/artikel_list.html"
    context = {
        "title": "Welcome to My Site"
    }
    return render(request, template_name, context)

def artikel_by_kategori(request, kategori_id):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.filter(kategori_id=kategori_id)
    context = {
        "title": "Welcome to My Site",
        "kategori": kategori,
        "artikel": artikel,
    }
    return render(request, template_name, context)



