from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.uix.label import Label
import random

class CodificadorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=30, **kwargs)

        self.mapping = {}
        self.reverse_mapping = {}

        # Caixa de entrada (texto original)
        self.input_box = TextInput(
            hint_text='Escreve o texto para codificar...',
            multiline=True,
            font_size='22sp',
            size_hint_y=0.5
        )
        self.add_widget(self.input_box)

        # Caixa de saída (texto codificado)
        self.output_box = TextInput(
            hint_text='Texto codificado ou descodificado aparecerá aqui...',
            multiline=True,
            readonly=True,
            font_size='22sp',
            size_hint_y=0.5
        )
        self.add_widget(self.output_box)

        # Linha de botões
        buttons = BoxLayout(size_hint_y=0.2, spacing=10)
        encode_button = Button(text='Codificar', font_size='22sp', background_color=(0.2, 0.6, 1, 1))
        encode_button.bind(on_press=self.codificar)
        decode_button = Button(text='Descodificar', font_size='22sp', background_color=(0.3, 0.8, 0.3, 1))
        decode_button.bind(on_press=self.descodificar)
        copy_button = Button(text='Copiar', font_size='22sp', background_color=(0.9, 0.6, 0.2, 1))
        copy_button.bind(on_press=self.copiar)
        buttons.add_widget(encode_button)
        buttons.add_widget(decode_button)
        buttons.add_widget(copy_button)
        self.add_widget(buttons)

        # Mensagem inferior
        self.status = Label(text='', font_size='18sp', size_hint_y=0.1)
        self.add_widget(self.status)

    def codificar(self, instance):
        texto = self.input_box.text.strip()
        if not texto:
            self.status.text = '⚠️ Escreve algo para codificar.'
            return

        indices = list(range(len(texto)))
        random.shuffle(indices)
        self.mapping = {i: indices[i] for i in range(len(texto))}
        self.reverse_mapping = {v: k for k, v in self.mapping.items()}

        resultado = ''.join([texto[self.mapping[i]] for i in range(len(texto))])
        self.output_box.text = resultado
        self.status.text = '✅ Texto codificado!'

    def descodificar(self, instance):
        texto = self.output_box.text.strip()
        if not texto:
            self.status.text = '⚠️ Não há texto para descodificar.'
            return
        if not self.reverse_mapping:
            self.status.text = '⚠️ O mapa de codificação foi perdido (precisas codificar primeiro).'
            return

        resultado = ''.join([texto[self.reverse_mapping[i]] for i in range(len(texto))])
        self.output_box.text = resultado
        self.status.text = '✅ Texto descodificado!'

    def copiar(self, instance):
        texto = self.output_box.text.strip()
        if texto:
            Clipboard.copy(texto)
            self.status.text = '📋 Copiado para a área de transferência.'
        else:
            self.status.text = '⚠️ Nada para copiar.'

class CodificadorApp(App):
    def build(self):
        self.title = 'Codificador Enigma'
        return CodificadorLayout()

if __name__ == '__main__':
    CodificadorApp().run()
