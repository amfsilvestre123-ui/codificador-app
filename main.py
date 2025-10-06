from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random, string

# dicionário de chaves
chaves = {}

class MainLayout(BoxLayout):
    def codificar(self):
        texto_original = self.ids.entrada.text.strip()
        palavras = texto_original.split()
        mapa = {}
        resultado = []

        for palavra in palavras:
            if len(palavra) > 0:
                pos = random.randint(0, len(palavra)-1)
                letra_nova = random.choice(string.ascii_lowercase)
                while letra_nova == palavra[pos].lower():
                    letra_nova = random.choice(string.ascii_lowercase)

                palavra_codificada = palavra[:pos] + letra_nova + palavra[pos+1:]
                mapa[palavra_codificada] = palavra
                resultado.append(palavra_codificada)
            else:
                resultado.append(palavra)

        texto_codificado = " ".join(resultado)
        chaves[texto_codificado] = mapa
        self.ids.saida.text = texto_codificado

    def decodificar(self):
        texto_codificado = self.ids.entrada.text.strip()
        palavras = texto_codificado.split()

        if texto_codificado not in chaves:
            self.ids.saida.text = "Erro: não existe chave para este texto!"
            return

        mapa = chaves[texto_codificado]
        resultado = [mapa.get(p, p) for p in palavras]
        self.ids.saida.text = " ".join(resultado)


class CodificadorApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    CodificadorApp().run()
