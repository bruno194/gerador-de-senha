import PySimpleGUI as sg
import random

sg.theme('SystemDefaultForReal')
def principal():
    estilo = [
        [sg.Text('SUGESTÃO DE SENHA')],
        [sg.Button('gerar senha')],
        [sg.Text(size=(30,10), key='converter')],
        [sg.Button('sair')]
    ]
    janela = sg.Window('CONVERSOR DE TEXTO').layout(estilo)
    while True:
        evento, valores = janela.read()
        cores = random.choice(['green', 'yellow', 'red', 'black', 'blue'])
        a = random.choice('abcdefghijklmnopqrstuvwxyz')
        b = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        c = random.choice('123456789')
        d = random.choice('#$%¨&*@!_+=°?**/#')
        e = random.choice('FFFFFFFfffff')
        f = random.choice('{ ~^^: ( .  nh, . ')
        g = random.choice('123456789')
        if evento == sg.WINDOW_CLOSED or evento == 'sair':
            break
        if evento == 'gerar senha':
            janela['converter'].update(f'{a} {b} {c} {d} {e} {f} {g}', text_color=cores)

principal()