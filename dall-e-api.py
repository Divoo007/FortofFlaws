import os
import openai
openai.api_key = "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"

def voice_generation(answerr):
    from gtts import gTTS
    import os
    name = str(input())
    language = 'en'
    myobj = gTTS(text=answerr, lang=language, slow=False)
    myobj.save(name + ".mp3")
    os.system("mpg321 welcome.mp3")

def splitting(answerr):
    answerr.split('.')
    return answerr


def image_generation(generationtext):
    temp = []
    for i in range(4):
        openai.Model.list()
        response = openai.Image.create(
        prompt=generationtext,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        temp.append(image_url)
    print(temp)
    

textt = str(input())
brotf = image_generation(textt)
print(brotf)





  

