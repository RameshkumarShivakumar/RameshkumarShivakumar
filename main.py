from kivymd.app import MDApp
from kivymd.uix.label import MDLabel 
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.carousel import Carousel
from kivy.core.window import Window
Window.size=(350,600)
Window.clearcolor=(1,0,1,1)
#Here Creating The Application Gladders
class Gladders(MDApp):
    def build(self):
        return StartingFluck()
class StartingFluck(MDFloatLayout):
    def data(self,*argv):
        make1=self.ids.string1.text
        make2=self.ids.string2.text
        make3=int(self.ids.string1.text)
        make4=int(self.ids.string2.text)
        make5=make3*make4
        makeing7=[]
        makeing7.append(str(make5))
        for a in makeing7:
            print(a)
        self.ids.ds.text=a
Gladders().run()