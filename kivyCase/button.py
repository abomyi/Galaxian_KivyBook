import kivy
from kivy.uix.boxlayout import BoxLayout
#from ibus.common import ORIENTATION_VERTICAL, ORIENTATION_HORIZONTAL
from kivy.uix.textinput import TextInput
kivy.require('1.9.1') # replace with your current kivy version !
 
from kivy.app import App
from kivy.uix.label import Label
 
 
class MyApp(App):
 
    def build(self):
        
        layout = BoxLayout(orientation='vertical') 
        
        hello = Label(text='Hello world',
                      font_size=150)
        
        text = TextInput()
        
        layout.add_widget(hello)
        layout.add_widget(text)
        
        return layout


if __name__ == '__main__':
    MyApp().run()