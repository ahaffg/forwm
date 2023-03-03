from django.shortcuts import render

# Create your views here.

def UserRegister(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'forum-login.html')        
    return render(request, "forum-register.html")


def UserLogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/myprofile")
        else:
            return HttpResponse("User not Found")
        alert = True
        return render(request, 'forum-login.html', {'alert':alert})            
    return render(request, "forum-login.html")


def myprofile(request):
    if request.method=="POST":
        user = request.user    
        profile = Profile(user=user)
        profile.save()
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "forum-profile.html",{'obj':obj})
    else:
        form=ProfileForm()
    return render(request, "forum-profile.html", {'form':form})


def forum(request):
    profile = Profile.objects.all()
    if request.method=="POST":   
        user = request.user
        image = request.user.profile.image
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content, image=image)
        post.save()
        alert = True
        return render(request, "forum.html", {'alert':alert})
    posts = Post.objects.all()
    return render(request, "forum.html", {'posts':posts})

<script>
     {% if alert %}
    alert('Your Question has been posted successfully!!');
    document.location = '/';
    {% endif %}
    </script>
    {% endblock %}

def discussion(request, myid):
    post = Post.objects.filter(id=myid).first()
    replies = Replie.objects.filter(post=post)
    if request.method=="POST":
        user = request.user
        image = request.user.profile.image
        desc = request.POST.get('desc','')
        post_id =request.POST.get('post_id','')
        reply = Replie(user = user, reply_content = desc, post=post, image=image)
        reply.save()
        alert = True
        return render(request, "discussion.html", {'alert':alert})
    return render(request, "discussion.html", {'post':post, 'replies':replies})