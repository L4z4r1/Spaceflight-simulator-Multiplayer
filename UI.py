from kivy.app import App

from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from functools import partial

Builder.load_file("GUI.kv")

class Multiplayer(App, BoxLayout):

    def build(self):
        sv = self.ids['scrollView']
        bl = self.ids['bl']
        #test = bl.sv
        # self.box = BoxLayout(orientation='horizontal', spacing=20)
        # self.txt = TextInput(text= "LOL", hint_text='Enter Multiplayer path...', size_hint=(.5,.1))
        # self.btn = Button(text='Clear', on_press=self.clearText, size_hint=(.1,.1))
        # self.abtn = Button(text='Save', on_press = self.savelocation, size_hint = (.1, .1))
        # self.down = Button(text='Download world', size_hint = (, ))
        # self.box.add_widget(self.txt)
        # self.box.add_widget(self.btn)
        # self.box.add_widget(self.abtn)
        # self.box.add_widget(self.down)
        # print(self.txt.text)
        # return self.box
        #self.lab = Label(text='test')
        return self

    # def clearText(self, instance):
    #     self.txt.text = ''

    def output(self, out):
        self.ids['l'].text = self.ids['l'].text + "\n" + out

    # def savelocation(self, instance):
    #     print("[+]", self.txt.text)
    #     Main.save(self.txt.text)

Multiplayer().run()
