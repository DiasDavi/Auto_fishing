import PySimpleGUI as sg
import pyautogui
import keyboard

def button_color(enabled):
    if enabled:
        return ('green', 'white')
    else:
        return ('red', 'white')

layout = [
    [sg.Text('Coordenadas do peixe no pluzze de pesca')],
    [sg.Text('X:'), sg.Input(key='X_FISH', size=(10,1), disabled=True), sg.Text('Y:'), sg.Input(key='Y_FISH', size=(10,1)), sg.Button('Começar a capturar',key='Button-1')],
    [sg.Text('Coordenadas do lago/mar')],
    [sg.Text('X:'), sg.Input(key='X_OCEAN_POSITION', size=(10,1), disabled=True), sg.Text('Y:'), sg.Input(key='Y_OCEAN_POSITION', size=(10,1)), sg.Button('Começar a capturar',key='Button-2')],
    [sg.Text('Coordenadas do seu pokemon')],
    [sg.Text('X:'), sg.Input(key='X_POKE', size=(10,1), disabled=True), sg.Text('Y:'), sg.Input(key='Y_POKE', size=(10,1)), sg.Button('Começar a capturar',key='Button-3')],
    [sg.Text('Coordenadas do pokemon derrotado')],
    [sg.Text('X:'), sg.Input(key='X_POKE_DEAD', size=(10,1), disabled=True), sg.Text('Y:'), sg.Input(key='Y_POKE_DEAD', size=(10,1)), sg.Button('Começar a capturar',key='Button-4')],
    [sg.Text('Coordenadas do loot do pokemon derrotado')],
    [sg.Text('X:'), sg.Input(key='X_BP_LOOT_POSITION', size=(10,1), disabled=True), sg.Text('Y:'), sg.Input(key='Y_BP_LOOT_POSITION', size=(10,1)), sg.Button('Começar a capturar',key='Button-5')],
    [sg.Text('Aperte com o botão esquerdo ou pressione "s" para salvar as posições', key='click', size=(50,1))],
    [sg.Text('Ligar bot ', key='click'),sg.Button('Desligado', key='toggle_button', button_color=button_color(False))],
    # [sg.Checkbox('Usar pokebolls', key='USE-POKEBALL')]
]

window = sg.Window('BOT DE PESCA', layout, keep_on_top=True)
# coordenadas do puzzle de pesca
X_FISH, Y_FISH = pyautogui.position()
RGB_FISH = pyautogui.screenshot().getpixel((X_FISH, Y_FISH))
# coordenadas do lago/mar
X_OCEAN_POSITION, Y_OCEAN_POSITION = pyautogui.position()
# coordenadas do seu poke
X_POKE, Y_POKE = pyautogui.position()
RGB_POKE = pyautogui.screenshot().getpixel((X_POKE, Y_POKE))
# coordenadas do poke derrotado
X_POKE_DEAD, Y_POKE_DEAD = pyautogui.position()
# coordenadas do loot
X_BP_LOOT_POSITION, Y_BP_LOOT_POSITION = pyautogui.position()
# lista de comandos
LIST_ATACK = ['f1','f2','f3','f4','f5','f6']
# Define se usará ou não pokeball
USE_POKEBALL = False
enabled = False

def captura_coordenadas_pesca():
    global X_FISH, Y_FISH, RGB_FISH
    if event == 'Button-1':
        while True:
            X_FISH, Y_FISH = pyautogui.position()
            RGB_FISH = pyautogui.screenshot().getpixel((X_FISH, Y_FISH))
            window['X_FISH'].update(X_FISH)
            window['Y_FISH'].update(Y_FISH)
            window.refresh()
            if keyboard.is_pressed('s'):
                break


def captura_coordenadas_lago():
    global X_OCEAN_POSITION, Y_OCEAN_POSITION
    if event == 'Button-2':
        while True:
            X_OCEAN_POSITION, Y_OCEAN_POSITION = pyautogui.position()
            window['X_OCEAN_POSITION'].update(X_OCEAN_POSITION)
            window['Y_OCEAN_POSITION'].update(Y_OCEAN_POSITION)
            window.refresh()
            if keyboard.is_pressed('s'):
                break

def captura_coordenadas_pokemon():
    global X_POKE, Y_POKE, RGB_POKE
    if event == 'Button-3':
        while True:
            X_POKE, Y_POKE = pyautogui.position()
            RGB_POKE = pyautogui.screenshot().getpixel((X_POKE, Y_POKE))
            window['X_POKE'].update(X_POKE)
            window['Y_POKE'].update(Y_POKE)
            window.refresh()
            if keyboard.is_pressed('s'):
                break

def captura_coordenadas_pokemon_derrotado():
    global X_POKE_DEAD, Y_POKE_DEAD
    if event == 'Button-4':
        while True:            
            X_POKE_DEAD, Y_POKE_DEAD = pyautogui.position()
            window['X_POKE_DEAD'].update(X_POKE_DEAD)
            window['Y_POKE_DEAD'].update(Y_POKE_DEAD)
            window.refresh()
            if keyboard.is_pressed('s'):
                break

def captura_coordenadas__loot_pokemon_derrotado():
    global X_BP_LOOT_POSITION, Y_BP_LOOT_POSITION
    if event == 'Button-5':
        while True:            
            X_BP_LOOT_POSITION, Y_BP_LOOT_POSITION = pyautogui.position()
            window['X_BP_LOOT_POSITION'].update(X_BP_LOOT_POSITION)
            window['Y_BP_LOOT_POSITION'].update(Y_BP_LOOT_POSITION)
            window.refresh()
            if keyboard.is_pressed('s'):
                break

def ligar_bot():
    global enabled
    if event == 'toggle_button':
        enabled = not enabled
        window['toggle_button'].update(button_color=button_color(enabled))
        window['toggle_button'].update(text='Ligado' if enabled else 'Desligado')

# função que clica no peixe
def click_fish():
    pyautogui.moveTo(X_FISH, Y_FISH)
    pyautogui.click()

# função que usa os ataques
def poke_atack():
    pyautogui.press(LIST_ATACK)

# função que usa pega o loot
def get_loot():
    pyautogui.moveTo(X_POKE_DEAD, Y_POKE_DEAD)
    pyautogui.click(button='right')
    pyautogui.sleep(0.8)
    pyautogui.moveTo(X_BP_LOOT_POSITION, Y_BP_LOOT_POSITION)
    pyautogui.click(clicks=5)

# função para capturar pokemon
def use_pokeball():
    if USE_POKEBALL:
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.moveTo(X_POKE_DEAD, Y_POKE_DEAD)
        pyautogui.click()
    
# função para caso seu pokemon sai do lugar
def check_poke_position():
    pyautogui.moveTo(X_POKE,Y_POKE)
    pyautogui.press('f11')
    pyautogui.click()

def use_rod():
    pyautogui.press('delete')
    pyautogui.moveTo(X_OCEAN_POSITION, Y_OCEAN_POSITION)
    pyautogui.click()

while True:
    event, values = window.read(timeout=10)
    if event == sg.WINDOW_CLOSED:
        break

    captura_coordenadas_pesca()
    captura_coordenadas_lago()
    captura_coordenadas_pokemon()
    captura_coordenadas_pokemon_derrotado()
    captura_coordenadas__loot_pokemon_derrotado()
    ligar_bot()

    fish = pyautogui.pixelMatchesColor(X_FISH,Y_FISH,RGB_FISH)
    if fish == True and enabled == True:
        click_fish()
        pyautogui.sleep(1.2)        
        poke_atack()
        pyautogui.sleep(2)
        get_loot()
        pyautogui.sleep(2)
        use_pokeball()
        pyautogui.sleep(2)
        check_poke_position()
        pyautogui.sleep(2)
        use_rod()
        pyautogui.sleep(2)

window.close()
