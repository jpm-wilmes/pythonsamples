# Python program controlling Dexarm robot
# Learn robot and replay
import time
# make use of gui
import PySimpleGUI as sg
# controlling the robot
from pydexarm import Dexarm
# create robot object by connecting
dexarm = Dexarm(port="COM5")
# global playback history
history=[]

# robot commands processor
def send_robot(x,y,z,f,save):
    # x,y,z contain delta (+1, 0 or -1)
    # f contains function: 'reset', 'open', 'close', 'move', 'huis'
    # save enables storage of commands
    positie=dexarm.get_current_position()
    if f=='reset':
        dexarm.go_home()
        dexarm.air_picker_stop()
        history.clear()
    elif f=='huis':
        dexarm.go_home()
        dexarm.air_picker_stop()
    elif f=='move':
        dexarm.move_to(positie[0]+x, positie[1]+y, positie[2]+z)
    elif f=='open':
        dexarm.air_picker_pick()
    elif f=='close':
        dexarm.air_picker_place()

    command=[x,y,z,f]
    # only save when not in replay mode
    if save:
        history.append(command)
    return

# commands player (replay history)
def replay_robot():
    for action in history:
        print('actie:',action)
        send_robot(action[0], action[1], action[2], action[3], False)
        time.sleep(0.5)
     
################################################### MAIN #################################################
sg.theme('DarkAmber')
# variables for screen layout
layout = [   
    [sg.Text('Leer robot programmeren')],
    [sg.Button("Reset")],
    [sg.Button("Huis")],
    [sg.Button("Voren")],
    [sg.Button('Links'), sg.Button('Rechts')],
    [sg.Button('Omhoog'), sg.Button('Omlaag')],
    [sg.Button("Achteren")],
    [sg.Button('Open'), sg.Button('Dicht')],
    [sg.Button("Replay")],
]
windowsize=(300,300)
windowslocation=(0,0)

# create window   
window = sg.Window('Schermtitel', layout, size=windowsize, location=windowslocation,  element_justification='c')

while True:
    event, values=window.read()
    # cancel/end program
    if event == sg.WIN_CLOSED:
        print('jammer, afgelopen')
        break
    # else
    elif event == 'Reset':
        send_robot(0,0,0,'reset',False)
    elif event == 'Huis':
        send_robot(0,0,0,'huis',True)
    elif event == 'Links':
        send_robot(-10,0,0,'move', True)
    elif event == 'Rechts':
        send_robot(10,0,0,'move', True)
    elif event == 'Omhoog':
        send_robot(0,0,10,'move', True)
    elif event == 'Omlaag':
        send_robot(0,0,-10,'move', True)
    elif event == 'Voren':
        send_robot(0,10,0,'move', True)
    elif event == 'Achteren':
        send_robot(0,-10,0,'move', True)
    elif event == 'Open':
        send_robot(0,0,0,'open', True)
    elif event == 'Dicht':
        send_robot(0,0,0,'close', True)
    elif event == 'Replay':
        replay_robot()

window.close()