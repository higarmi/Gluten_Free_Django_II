from main.models import recipe, comment
from main.forms import recipeForm, commentForm, contactForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def about(request):
	html = "<html><body>Sample Project in MDW</body></html>"
	return HttpResponse(html)

def begin(request):
    recipes = recipe.objects.all()
    return render_to_response('begin.html',{'recipes':recipes}, context_instance=RequestContext(request))

def users(request):
    users = User.objects.all()
    recipes = recipe.objects.all()
    return render_to_response('users.html',{'users':users,'recipes':recipes}, context_instance=RequestContext(request))

def recipes_list(request):
    recipes = recipe.objects.all()
    return render_to_response('recipes.html',{'datos':recipes}, context_instance=RequestContext(request))

def detail_recipe(request, id_recipe):
    dato = get_object_or_404(recipe, pk=id_recipe)
    comments = comment.objects.filter(recipe=dato)
    return render_to_response('recipe.html',{'recipe':dato,'comments':comments}, context_instance=RequestContext(request))

def contact(request):
    if request.method=='POST':
        formA = contactForm(request.POST)
        if formA.is_valid():
            title = 'message from our Recipe Center'
            body = formA.cleaned_data['message'] + "\n"
            body += 'Connect with: ' + formA.cleaned_data['email']
            email = EmailMessage(title, body, to=['johndoe@email.com'])
            email.send()
            return HttpResponseRedirect('/')
    else:
        formA = contactForm()
    return render_to_response('contactform.html',{'formA':formA}, context_instance=RequestContext(request))

def new_recipe(request):
    if request.method=='POST':
        formA = recipeForm(request.POST, request.FILES)
        if formA.is_valid():
            formA.save()
            return HttpResponseRedirect('/recipes')
    else:
        formA = recipeForm()
    return render_to_response('recipeform.html',{'formA':formA}, context_instance=RequestContext(request))


def new_comment(request):
    if request.method=='POST':
        formA = commentForm(request.POST)
        if formA.is_valid():
            formA.save()
            return HttpResponseRedirect('/recipes')
    else:
        formA = commentForm()
    return render_to_response('commentform.html',{'formA':formA}, context_instance=RequestContext(request))

def new_user(request):
    if request.method=='POST':
        formA = UserCreationForm(request.POST)
        if formA.is_valid:
            formA.save()
            return HttpResponseRedirect('/')
    else:
        formA = UserCreationForm()
    return render_to_response('newuser.html',{'formA':formA}, context_instance=RequestContext(request))

def enter(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/private')
    if request.method == 'POST':
        formA = AuthenticationForm(request.POST)
        if formA.is_valid:
            user = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=user, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/private')
                else:
                    return render_to_response('notactive.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nouser.html', context_instance=RequestContext(request))
    else:
        formA = AuthenticationForm()
    return render_to_response('enter.html',{'formA':formA}, context_instance=RequestContext(request))

@login_required(login_url='/enter')
def private(request):
    user = request.user
    return render_to_response('private.html', {'user':user}, context_instance=RequestContext(request))

@login_required(login_url='/enter')
def close(request):
    logout(request)
    return HttpResponseRedirect('/')