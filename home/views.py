from django.shortcuts import render
from django.http import HttpResponse
from.models import Audio
# Create your views here.
def home(request):
    ctx={'audiolist': Audio.objects.all()}
    return render(request, 'home.html', {})

def upload(request):
    form_files= request.FILES
    ctx= {}
    if form_files:
        file = form_files['file']
        image = form_files['image']
        user= request.user or 1 # if no user,use user with id 1
        Audio.objrcts.create(file=file,user=user,thumbnail=image)
        ctx['success'] =True
    else:
        ctx['success'] = False
        audios =Audio.objects.all()
        ctx['audiolist']= audios
        return render(request,'partials/audio_app.html', ctx)
