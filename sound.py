from gtts import gTTS
from playsound import playsound



myAudio=gTTS(text="your showing your forefinger",lang='en',slow=False)
my=gTTS(text=" I am ok ",lang='en',slow=False)
myAudio.save("bj.mp3")
my.save("ok.mp3")
class Play:
    def start(self,a=False):
       playsound("D:\pythonProject/bj.mp3")

    def ok(self,a=False):
       playsound("D:\pythonProject/ok.mp3")








