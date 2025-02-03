from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseForbidden
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'article_list.html',context=context)

def article_detail(request,id):
    article = get_object_or_404(Article,id=id)
    context = {
        'article':article
    }
    return render(request,'article_detail.html',context=context)

def article_edit(request,id):
    article = get_object_or_404(Article,id=id)
    if request.user != article.author:
        return HttpResponseForbidden("❌ Siz ushbu maqolani tahrirlash huquqiga ega emassiz.")
    if request.method == 'POST':
        form=ArticleForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail',id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form':form,
        'article':article
    }
    return render(request,'article_edit.html',context=context)

@login_required
def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail',id=article.id)
    else:
        form=ArticleForm()

    context = {
        'form':form
    }
    return render(request,'article_add.html',context=context)

def article_delete(request,id):
    article = get_object_or_404(Article,id=id)
    if request.user != article.author:
        return HttpResponseForbidden('❌ Siz ushbu maqolani ochirish huquqiga ega emassiz.')
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    context = {
        'article':article
    }
    return render(request,'article_delete.html',context=context)

def homepage(request):
    return render(request,'home.html')

