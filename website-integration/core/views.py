from django.shortcuts import render, redirect
from django.http import HttpResponse
import jaiganesh.settings as site_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from .main import mainf





def home(request):
    if request.method == 'POST':
        textt = request.POST['searched']
        output = mainf(textt)
        return redirect('/media/my_video.mp4')
    else:
        submitted = False
        meta = {'title': 'Home | staticstartup'}
        usr =None
        context = {'meta': meta}
        return render(request, 'index.html', context)


def main(request):
    if request.method == 'POST':
        textt = request.POST['searched']
        output = mainf(textt)
        return redirect('/media/my_video.mp4')
    else:
        context = {'bruh':'bruh'}
        return render(request, 'main.html', context)

def mainf(user_text):
    import os
    import openai as ai
    from requests import get
    import random as rn
    from uuid import uuid1
    from gtts import gTTS
    import moviepy.editor as mpe
    import moviepy.video.io.ImageSequenceClip
    from django.conf import settings

    ai.api_key = "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"

    def generate_gpt3_response(user_text):
        completions = ai.Completion.create(
            engine='text-davinci-003',  
            temperature=0.5,            
            prompt=user_text,           
            max_tokens=100,             
            n=1,                        
            stop=None,                  
        )
        return completions.choices[0].text

    generationtext = generate_gpt3_response(user_text)

    final = []

    def image_generation(generationtext):
        temp = []
        for i in range(4):
            ai.Model.list()
            response = ai.Image.create(
                prompt=generationtext,
                n=1,
                size="256x256"
                )
            image_url = response['data'][0]['url']
            temp.append(image_url)
        return temp

    random2 = image_generation(generationtext)

    downloadFlag = False

    def downloadimg(url):
        response = get(url)
        df = str(uuid1())
        with open("/tmp/images/"+df+".png", "wb") as f:
            f.write(response.content)
        
        
    for i in random2:
        downloadimg(i)

    downloadFlag = True

    image_folder='/tmp/images/'

    if downloadFlag:
        image_files = [os.path.join(image_folder,img)
                    for img in os.listdir(image_folder)
                    if img.endswith(".png")]
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps = 0.1)
        clip.write_videofile('/tmp/my_video.mp4')



    def texttospeech(answerr):
        language = 'en'
        myobj = gTTS(text=answerr, lang=language, slow=False)
        myobj.save("/tmp/somename.mp3")
        os.system("mpg321 /tmp/somename.mp3")

    texttospeech(generationtext)

    def combine_audio(vidname, audname, outname, fps=60): 
        my_clip = mpe.VideoFileClip(vidname)
        audio_background = mpe.AudioFileClip(audname)
        final_clip = my_clip.set_audio(audio_background)
        final_clip.write_videofile(outname,fps=fps)

    combine_audio("/tmp/my_video.mp4", "/tmp/somename.mp3", "/Users/divyansh/Documents/web_projects/jaiganesh/media/my_video.mp4")    
    
    for i in range(4):
        os.remove(image_files[i])
    return redirect('/media/my_video.mp4') 
