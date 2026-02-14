print("Mee0w from ModuPad_v2!")
print("Launching Mee0w... inthe KMK world!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

#-----------------------------------------------------------------------------------

keyboard = KMKKeyboard()

# ==============================
#Switch setup
# ==============================

keyboard.col_pins = (board.D9, board.D15, board.D18, board.D19 board.D21)
keyboard.row_pins = (board.D4, board.D5, board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 5x5 matrix

keyboard.keymap = [

    [KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,
     KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N10,
     KC.N11, KC.N12, KC.N13, KC.N14, KC.N15,
     KC.N16, KC.N17, KC.N18, KC.N19, KC.N20,
     KC.N21, KC.N22, KC.N23, KC.N24, KC.N25],      
    
    ],

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()