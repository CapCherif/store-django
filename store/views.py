

from django.shortcuts import redirect, render

from article.models import Article


def Index(request):
    articles = Article.objects.all() # lecture de la bd
   
    return render(request, "index.html", {"articles":articles})


def Ajout(request):
    added = False
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        date = request.POST['date']
        print(title, author, description, date)
        # créer un objet de Article
        article = Article()
        # remplir cet objet
        article.title = title
        article.description = description
        article.author = author
        article.date = date
        added = True
        article.save() # save to database
    return render(request, "ajout.html", {'added':added})


def Detail(request):
    # récupérer l'id depuis le lien detail?id=3...
    idarticle = request.GET.get('id')

    # filtrer la base de donnée (sqlite3)
    article = Article.objects.get(id=idarticle)
    
    # passer l'article comme paramétre a la page detail
    return render(request, "detail.html", {"article":article})


def Delete(request):

    # récupérer l'id depuis le lien detail?id=3...
    idarticle = request.GET.get('id')

    Article.objects.filter(id=idarticle).delete()
    return redirect('/')


def Update(request):
    idarticle = request.GET.get('id')
    article = Article.objects.get(id=idarticle)
    print(article)
    return render(request, "update.html", {"article":article})


def UpdateArticle(request):
    idarticle = request.POST['id']
    article = Article.objects.get(id=idarticle)
    #modifier l'article
    article.title = request.POST['title']
    article.date = request.POST['date']
    article.description = request.POST['description']
    article.author = request.POST['author']

    article.save()

    return redirect('/detail?id='+str(idarticle))