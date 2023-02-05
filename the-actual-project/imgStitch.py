import os
import moviepy.video.io.ImageSequenceClip
from gtts import gTTS
from imgVoiceSplitting import downloadFlag, gptResult
image_folder='./images/'



if downloadFlag:
    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps = 0.1)
    clip.write_videofile('my_video.mp4')



def texttospeech(answerr):

    language = 'en'
    myobj = gTTS(text=answerr, lang=language, slow=False)
    myobj.save("somename.mp3")
    os.system("mpg321 somename.mp3")

texttospeech(gptResult)

def combine_audio(vidname, audname, outname, fps=60): 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

combine_audio("my_video.mp4", "somename.mp3", "my_video.mp4") # i rewrite on the same file                                                                                   