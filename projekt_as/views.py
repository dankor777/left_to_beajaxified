from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Komentarz, KomentarzX
from .forms import PostForm, KomentarzForm, KomentarzXForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.contrib.auth.models import Group


#def home(request):
#    return render(request, 'index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 2

class Postview(DetailView):
    model = Post
    template_name = 'post_widok.html'

class DodajPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dodaj_post.html'
    # fields = '__all__'

class EdytujPostView(UpdateView):
    model = Post
    template_name = 'edycja_postu.html'
    fields = ['tytul', 'tresc']

class UsunPostView(DeleteView):
    model = Post
    template_name = 'usun_post.html'
    success_url = reverse_lazy('index')

# class DodajKomnetarzView(CreateView):
#     model = Komentarz
#     form_class = KomentarzForm
#     template_name = 'dodaj_komentarz.html'
#     def form_valid(self,form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
#     success_url = reverse_lazy('index')
def searchPost(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(tytul__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'posts':posts})
    else:
        return render(request, 'search.html', {'searched':searched})

def post_detail(request,id):
    post = get_object_or_404(Post, id=id)
    comments = KomentarzX.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = KomentarzXForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = KomentarzX.objects.get(id=reply_id)
            comment = KomentarzX.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return redirect('post_detail', id=id)
    else:
        comment_form = KomentarzXForm()
    context = {
        'post':post,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'post_widok.html',context)
