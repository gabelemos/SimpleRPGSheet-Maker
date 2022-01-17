from random import choices
from tkinter import font
from typing import Sized, Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, Input, SELECT_MODE_EXTENDED

sg.theme('DarkBlue4') #cor tema :D

estilos = ('Estilo_1', 'Estilo_2', 'Estilo_3', 'Estilo_4', 'Estilo_5')

bordaprincipal = '~' * 20

borda_1 = '-' * 20
borda_2 = '~' * 20
borda_3 = '*' * 20
borda_4 = '$' * 20
borda_5 = '¨' * 20

class TelaFicha:
    def __init__(self):
        
         #layout
         layout = [ [sg.Text('Nome: ', size=(6,0)), sg.Input(size=(16,0),key='nome')],
           [sg.Text('Idade: ', size=(6,0)), sg.Input(size=(3,0),key='idade'), sg.Listbox(estilos, size=(15,0), key='cor')],
           [sg.Text('Qual o gênero do seu personagem?'),sg.Radio('Masculino', 'sexos',key='masculino'), sg.Radio('Feminino', 'sexos',key='feminino')],
           [sg.Text('Outro: ',size=(6,0)), sg.Input(size=(16,0), key='outro')],
           [sg.Text('Qual a sexualidade do seu personagem?')],
           [sg.Text('Sexo: ',size=(6,0)), sg.Input(size=(16,0), key='outro_g')],
           [sg.Text('Gostos: ', size=(6,0)), sg.Input(size=(16,0), key='gostos')],
           [sg.Text('História: ', size=(6,0))],
           [sg.Multiline(font=('Consolas', 12), size=(30,10), key='historia')],
           [sg.Text('Ficha: ', size=(6,0))],
           [sg.Output(size=(40,10))],
           [sg.Button('Concluir Ficha'), sg.Button('Cancelar Ficha')] ]

        
         #janela
         self.janela = sg.Window('Criador de Ficha by L3M0S').layout(layout)
         
    def Iniciar(self):
        while True:
            #extraindo os dados
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            outro = self.values['outro']
            gostos = self.values['gostos']
            genero = self.values['outro_g']
            historia = self.values['historia']
            if self.values['outro'] != '':
                sexo = outro
            if self.values['masculino'] == True and self.values['feminino'] == False:
                sexo = 'Masculino'
            if self.values['feminino'] == True and self.values['masculino'] == False:
                sexo = 'Feminino'
            print('~' * 20),
            print('📓 Nome: {}'.format(nome)),
            print('🔢 Idade: {}'.format(idade)),
            print('🚻 Gênero: {}'.format(sexo)),
            print('🔁 Sexualidade: {}'.format(genero)),
            print('🎁 Gostos: {}'.format(gostos)),
            if self.values['cor'] == 'Estilo_1':
                bordaprincipal = borda_1
            if self.values['cor'] == 'Estilo_2':
                bordaprincipal = borda_2
            if self.values['cor'] == 'Estilo_3':
                bordaprincipal = borda_3
            if self.values['cor'] == 'Estilo_4':
                bordaprincipal = borda_4
            if self.values['cor'] == 'Estilo_5':
                bordaprincipal = borda_5
            print(bordaprincipal)
            print('📒 História: {}'.format(historia)),
            print(bordaprincipal)
            if self.button == sg.WIN_CLOSED:
                break
            if self.button == 'Cancelar Ficha':
                import os
                print("\n" * os.get_terminal_size().lines)
            


tela = TelaFicha()
tela.Iniciar()

