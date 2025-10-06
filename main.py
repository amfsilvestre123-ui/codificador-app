from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import random
import string

class CodificadorLayout(BoxLayout):
    input_text = StringProperty("")
    output_text = StringProperty("")

    def code_text(self):
        words = self.input_text.split()
        coded_words = []
        for word in words:
            if len(word) > 1:
                idx = random.randint(0, len(word) - 1)
                new_letter = random.choice(string.ascii_lowercase)
                coded_words.append(word[:idx] + new_letter + word[idx+1:])
            else:
                coded_words.append(word)
        self.output_text = " ".join(coded_words)

    def uncode_text(self):
        # (Simplesmente mostra o texto original)
        self.output_text = self.input_text

class CodificadorApp(App):
    def build(self):
        self.title = "Codificador de Texto"
        return CodificadorLayout()

if __name__ == "__main__":
    CodificadorApp().run()
