print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.extensions.international import International
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

combos = Combos()
macros = Macros()

keensy = KMKKeyboard()

keensy.extensions.append(International())
keensy.extensions.append(MediaKeys())
keensy.modules.append(combos)
keensy.modules.append(macros)
keensy.modules.append(Layers())

keensy.col_pins = (
                     board.GP15,
                     board.GP14,
                     board.GP13,
                     board.GP12,
                     board.GP11,
                     board.GP10,
                     board.GP9,
                     board.GP8,
                     board.GP7,
                     board.GP6,
                     board.GP5,
                     board.GP4,
                     board.GP3,
                     board.GP2,
                     board.GP1,                  )

keensy.row_pins = (




                     board.GP21,
                     board.GP20,
                     board.GP19,
                     board.GP18,
                     board.GP17,
                     board.GP16
                  )


keensy.diode_orientation = DiodeOrientation.COL2ROW
# DiodeOrientation.ROW2COL


ARFKEY = KC.MACRO("arf20")

MOMENTARY = KC.MO(1)

keensy.keymap = [
 [
   KC.CAPSLOCK,      KC.F1,      KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,      KC.F7,    KC.F8,    KC.F9,    KC.F10,     KC.F11,       KC.F12,         KC.PSCREEN, KC.INSERT,
   KC.GRAVE,         KC.N1,      KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,      KC.N7,    KC.N8,    KC.N9,    KC.N0,      KC.MINUS,     KC.EQUAL,       KC.BSPACE,  KC.DELETE,
   KC.TAB,           KC.Q,       KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,       KC.U,     KC.I,     KC.O,     KC.P,       KC.LBRACKET,  KC.RBRACKET,    KC.ENTER,   KC.END,
   KC.ESCAPE,        KC.A,       KC.S,     KC.D,     KC.F,     KC.G,     KC.H,       KC.J,     KC.K,     KC.L,     KC.SCOLON,  KC.QUOTE,     KC.NONUS_HASH,  KC.NO,      KC.PGUP,
   KC.LSHIFT,KC.NONUS_BSLASH,    KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,       KC.N,     KC.M,     KC.COMMA, KC.DOT,     KC.SLASH,     KC.RSHIFT,      KC.UP,      KC.PGDOWN,
   KC.LCTRL,         KC.LGUI,    KC.LALT,  KC.NO,    KC.NO,    KC.NO,    KC.SPACE,   KC.NO,    KC.NO,    KC.RALT,  MOMENTARY,  KC.RCTRL,     KC.LEFT,        KC.DOWN,    KC.RIGHT,
 ],
 [
   KC.NO,            KC.MUTE,    KC.VOLD,  KC.VOLU,  KC.MPLY,  KC.NO,    KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,        KC.NO,          KC.NO,      KC.NO,
   KC.NO,            KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,        KC.NO,          KC.NO,      KC.NO,
   KC.NO,            KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,        KC.NO,          KC.NO,      KC.HOME,
   KC.NO,            KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,        KC.NO,          KC.NO,      KC.NO,
   KC.NO,            ARFKEY,     KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,        KC.NO,          KC.NO,      KC.NO,
   KC.NO,            KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,    KC.NO,    KC.NO,    KC.NO,      KC.NO,        KC.NO,          KC.NO,      KC.NO,
 ]
]

combos.combos = [
]


if __name__ == '__main__':
    keensy.go()
