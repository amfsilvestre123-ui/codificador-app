from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import random
import string

# Guardar mapeamentos de codificação
original_to_coded = {}
coded_to_original = {}

class CodificadorLayout(BoxLayout):
    input_text = StringProperty("")
    output_text = StringProperty("")

    def code_text(self):
        global original_to_coded, coded_to_original
        original_to_coded = {}
        coded_to_original = {}

        words = self.input_text.split()
        coded_words = []

        for word in words:
            if len(word) > 2:
                idx = random.randint(0, len(word) - 1)
                new_letter = random.choice(string.ascii_lowercase)
                coded_word = word[:idx] + new_letter + word[idx+1:]
            else:
                coded_word = word
            coded_words.append(coded_word)
            original_to_coded[word] = coded_word
            coded_to_original[coded_word] = word

        self.output_text = " ".join(coded_words)

    def uncode_text(self):
        global coded_to_original
        words = self.input_text.split()
        decoded_words = []
        for word in words:
            if word in coded_to_original:
                decoded_words.append(coded_to_original[word])
            else:
                decoded_words.append(word)
        self.output_text = " ".join(decoded_words)

class CodificadorApp(App):
    def build(self):
        self.title = "Codificador de Texto"
        return CodificadorLayout()

if __name__ == "__main__":
    CodificadorApp().run()
