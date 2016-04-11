from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

class Boom(Image):
    sound = SoundLoader.load('boom.wav')
    
    def __init__(self, **kwargs):   #書本寫 def boom(self...) 是錯的，應為__init__(self...)
        self.__class__.sound.play()
        super(Boom, self).__init__(**kwargs)