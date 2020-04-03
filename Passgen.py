from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
import re
import random

Builder.load_file('./passgen.kv')
Window.size = (450, 450)

class PassgenWidget(Widget):
    n = StringProperty("4")
    passw=""
    def on_button_click(self,widget):
        # n = int(widget.slider.value)
        # if n>50:
        #     print("Up to 50 , You Sadist Fuck!!!")
        #     exit()

        password= ""

        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

        dig=random.choice(DIGITS)
        lo=random.choice(LOCASE_CHARACTERS)
        up=random.choice(UPCASE_CHARACTERS)
        sym=random.choice(SYMBOLS)
        password=dig+lo+up+sym
        TOTAL=DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS

        for i in range(0,int(self.n)-4):
            password+=random.choice(TOTAL)

        # print(password)
        lst=list(password)
        # print(lst)
        random.shuffle(lst)
        self.passw="".join(lst)
        self.ids.input_box.text=f"{self.passw}"
        # print(self.passw)
        
    def on_slide(self,widget):
        self.n=str(int(widget.value))
        self.ids.label1.text=f"{self.n}"
        # print(self.n)



class Passgen(App):
    def build(self):
        return PassgenWidget()

if __name__ == "__main__":
    Passgen().run()