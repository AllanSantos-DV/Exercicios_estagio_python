from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput

from Funcoes import inverter_palavras, remover_duplicados, maior_palindrome, anagrama_palindrome, formatar_frase


class TelaPrincipal(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        Window.size = (800, 300)
        self.dropdown = DropDown()
        self.exercicios = [
            'Reverter a ordem das palavras',
            'Remover caracteres duplicados',
            'Encontrar a substring palindrômica',
            'Colocar em maiúscula a primeira letra de cada frase',
            'Verificar se é um anagrama de um palíndromo'
        ]
        self.input_text = TextInput(hint_text='Digite a entrada', size_hint=(1, 0.1))
        self.output_label = TextInput(size_hint=(1, 0.1), readonly=True, halign='center')
        self.exercicio_selecionado = None

        self.criar_menu()
        self.criar_interface()

    def criar_menu(self):
        for exercicio in self.exercicios:
            btn = Button(text=exercicio, size_hint_y=None, height=40)
            btn.bind(on_release=lambda button: self.selecionar_exercicio(button.text))
            self.dropdown.add_widget(btn)

    def criar_interface(self):
        box_principal = BoxLayout(orientation='vertical', size_hint=(1, 1), padding=30)

        iniciar_button = Button(text='Iniciar', size_hint=(1, 0.1))
        dropdown_button = Button(text='Exercícios', size_hint=(1, 0.1))
        dropdown_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, value: setattr(dropdown_button, 'text', value))
        iniciar_button.bind(on_release=self.iniciar_exercicio)

        box_principal.add_widget(dropdown_button)
        box_principal.add_widget(self.input_text)
        box_principal.add_widget(iniciar_button)
        box_principal.add_widget(self.output_label)

        self.add_widget(box_principal)

    def selecionar_exercicio(self, exercicio):
        self.exercicio_selecionado = exercicio
        self.dropdown.select(exercicio)
        self.dropdown.dismiss()

    def iniciar_exercicio(self, *args):
        exercicio = self.exercicio_selecionado
        entrada = self.input_text.text
        if entrada == "":
            self.output_label.text = "Insira uma entrada valida"
            return
        resultado = executar_exercicio(exercicio, entrada)
        self.output_label.text = resultado
        self.dropdown.dismiss()


def executar_exercicio(exercicio, entrada):
    if exercicio == 'Reverter a ordem das palavras':
        return inverter_palavras(entrada)
    elif exercicio == 'Remover caracteres duplicados':
        return remover_duplicados(entrada)
    elif exercicio == 'Encontrar a substring palindrômica':
        return maior_palindrome(entrada)
    elif exercicio == 'Colocar em maiúscula a primeira letra de cada frase':
        return formatar_frase(entrada)
    elif exercicio == 'Verificar se é um anagrama de um palíndromo':
        return anagrama_palindrome(entrada)
    else:
        return 'Exercício não encontrado.'


class ExerciciosApp(App):
    def build(self):
        return TelaPrincipal()


if __name__ == '__main__':
    ExerciciosApp().run()
