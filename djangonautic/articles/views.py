from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.utils import translation
   
# def generate_stie_map:
#     articles = Article.objects.all().order_by('date')
#     articles.


def is_ko(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        if request.session[translation.LANGUAGE_SESSION_KEY] == 'ko':
            return True
    return False
     

def lang_change(request,name): 

        for article in articles:
            article.body = article.body_ko
            article.title = article.title_ko
            article.description = article.description_ko



def article_list(request):

    # user_language = 'ko'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    articles = Article.objects.filter(is_ready=True).order_by('date')

    if is_ko(request):
        for article in articles:
            article.body = article.body_ko
            article.title = article.title_ko
            article.description = article.description_ko

    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    template_name = 'articles/article_detail.html'
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None
    next_title = None
    prev_title = None

    if article.nextNode:
        next_article = Article.objects.get(slug=article.nextNode)
        next_title = next_article.title
        if is_ko(request):
                next_title = next_article.title_ko

    if article.prevNode:
        prev_article = Article.objects.get(slug=article.prevNode)
        prev_title = prev_article.title
        if is_ko(request):
                prev_title = prev_article.title_ko

    

 # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'article': article,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'next_title': next_title,
                                           'prev_title': prev_title,
                                           })