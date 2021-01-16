import subprocess, PySimpleGUI as sg

sg.theme('DarkGrey13')

layout = [
    [sg.Text('=================== WIFI SENHAS ===================')],
    [sg.Button('Mostrar'), sg.Button('Sair')],
    [sg.Output(size=(50,20))]
]

janela = sg.Window('Gerenciador de WIFI', layout=layout)

dados = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('ISO-8859-1').split('\n')
wifis = [linha.split(':')[1][1:-1] for linha in dados if "Todos os Perfis de Usu\xa0rios" in linha]

while True:
    eventos, valores = janela.Read()

    if eventos == 'Sair':
        break

    for wifi in wifis:
        resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('ISO-8859-1').split('\n')
        resultados = [linha.split(':')[1][1:-1] for linha in resultados if 'Conte£do da Chave' in linha]

        try:
            print(f'Nome: {wifi}\nSenha: {resultados[0]}\n')

        except IndexError:
            print(f'Nome {wifi}\nSenha: Não foi possível encontrar\n')
    print('-----------------------------------\n')
