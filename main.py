import random
import string
import base64
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 15

    Label:
        text: "Codificador Enigma"
        font_size: '32sp'
        bold: True
        size_hint_y: None
        height: self.texture_size[1] + 10

    TextInput:
        id: input_text
        hint_text: "Escreve o texto aqui..."
        font_size: '24sp'
        size_hint_y: 0.4
        multiline: True

    BoxLayout:
        size_hint_y: None
        height: 80
        spacing: 20

        Button:
            text: "Codificar"
            font_size: '26sp'
            background_color: (0.2, 0.6, 1, 1)
            on_press: app.encode_text()

        Button:
            text: "Descodificar"
            font_size: '26sp'
            background_color: (0.3, 1, 0.4, 1)
            on_press: app.decode_text()

    Label:
        text: "Resultado:"
        font_size: '28sp'
        bold: True
        size_hint_y: None
        height: self.texture_size[1] + 10

    TextInput:
        id: output_text
        text: ""
        font_size: '24sp'
        size_hint_y: 0.4
        multiline: True
        readonly: True
        cursor_blink: False
        background_color: (0.15, 0.15, 0.15, 1)
        foreground_color: (1, 1, 1, 1)
        padding: [10, 10]
'''


class CodificadorApp(App):
    def build(self):
        return Builder.load_string(KV)

    def encode_text(self):
        texto = self.root.ids.input_text.text.strip()
        if not texto:
            self.root.ids.output_text.text = "[vazio]"
            return

        # Gera chave aleatória
        chave = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        random.seed(chave)
        alfabeto = string.ascii_letters + string.digits + " .,!?;:-_@#%&()/"

        mapa = list(alfabeto)
        random.shuffle(mapa)
        dicionario = dict(zip(alfabeto, mapa))

        resultado = ''.join([dicionario.get(c, c) for c in texto])

        # Codifica a chave em Base64 para ocultar
        chave_codificada = base64.b64encode(chave.encode()).decode()
        texto_codificado = f"#@{chave_codificada}#{resultado}"

        self.root.ids.output_text.text = texto_codificado

    def decode_text(self):
        texto = self.root.ids.input_text.text.strip()
        if not texto.startswith("#@"):
            self.root.ids.output_text.text = "Texto inválido (formato desconhecido)"
            return

        try:
            chave_codificada = texto.split("#")[1].replace("@", "")
            mensagem = texto.split("#", 2)[2]
            chave = base64.b64decode(chave_codificada.encode()).decode()

            random.seed(chave)
            alfabeto = string.ascii_letters + string.digits + " .,!?;:-_@#%&()/"
            mapa = list(alfabeto)
            random.shuffle(mapa)
            dicionario_inverso = dict(zip(mapa, alfabeto))

            resultado = ''.join([dicionario_inverso.get(c, c) for c in mensagem])
            self.root.ids.output_text.text = resultado

        except Exception as e:
            self.root.ids.output_text.text = f"Erro ao descodificar: {e}"


if __name__ == "__main__":
    CodificadorApp().run()
