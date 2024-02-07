print("Starting")

import board
import neopixel
import time

from display import init, home, clear, writeData

init()
home()
writeData("Booting...")


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.modules.encoder import EncoderHandler


pixels = neopixel.NeoPixel(
    board.GP28,
    100,
    pixel_order=neopixel.GRB,
    brightness=1
)

COLORS = [
    (32, 0, 0),
    (32, 16, 0),
    (0, 32, 0),
    (0, 32, 32),
    (0, 0, 32),
    (16, 0, 32),
    (32, 32, 32),
    (0, 0, 0),
]

pixel_idle_color = 0

keyboard = KMKKeyboard()
keyboard.extensions.append(StringyKeymaps())

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.GP26,board.GP27,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14)
keyboard.row_pins = (board.GP15,board.GP20,board.GP19,board.GP18,board.GP17,board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoder_handler.pins = ((board.GP21, board.GP22, None),)  # Encoder click is handled via key matrix (top right)

def handle_encoder_click(key, kb, kc, coord):
    print(f"encoder click")

def handle_encoder_rotate(key, kb, kc, coord):
    global pixel_idle_color
    if key.direction == 1: # left
        pixel_idle_color = (pixel_idle_color - 1) % len(COLORS)
        pass
    elif key.direction == 2: # right
        pixel_idle_color = (pixel_idle_color + 1) % len(COLORS)
        pass

    pixels.fill(COLORS[pixel_idle_color])

ENCODER_CLICK = make_key(on_press=handle_encoder_click)
ENCODER_ROTATE_LEFT = make_key(on_press=handle_encoder_rotate)
ENCODER_ROTATE_LEFT.direction = 1
ENCODER_ROTATE_RIGHT = make_key(on_press=handle_encoder_rotate)
ENCODER_ROTATE_RIGHT.direction = 2

___ = 'NO'
keyboard.keymap = [[
    'ESC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', ___, ENCODER_CLICK,
    'GRV', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N0', 'MINS', 'EQL', 'BSPC', 'INS',
    'TAB', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'LBRC', 'RBRC', 'BSLS', 'DEL',
    'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'SCLN', 'QUOT', 'ENT', 'HOME', 'PGUP',
    'LSFT', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'COMM', 'DOT', 'SLSH', 'RSFT', 'UP', 'END', 'PGDN',
    'LCTL', 'LGUI', 'LALT', 'SPC', 'RALT', 'RGUI', 'WINMENU', 'RCTL', ___, ___, 'LEFT', 'DOWN', 'RGHT',
]]

# leds go zig-zag so this needs to be manually defined
leds_order = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1, -1, 29, 28, 27,
    26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 30, 31, 32, 33,
    34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 59, 58, 57, 56, 55,
    54, 53, 52, 51, 50, 49, 48, 47, 14, 13, 60, 61, 62, 63, 64, 65,
    66, 67, 68, 69, 70, 71, 72, 45, 46, 83, 82, 81, 80, 79, 78, 77,
    76, -1, -1, 75, 74, 73]

def handle_before_press(key, kb, kc, coord):
    pixels.fill(COLORS[pixel_idle_color])
    pixels[leds_order[coord]] = (255, 0, 0)
    
    return True

def handle_after_press(key, kb, kc, coord):
    # print(f"after press: {key}")
    return True


# Attach press event handlers
for key_name in keyboard.keymap[0]:
    # Skip special keys (encoder)
    if type(key_name) != str:
        continue

    KC[key_name].before_press_handler(handle_before_press)
    KC[key_name].after_press_handler(handle_after_press)

encoder_handler.map = [
    ((ENCODER_ROTATE_RIGHT, ENCODER_ROTATE_LEFT, None),)
]

home()
clear()
writeData("Hello :)")

pixels.fill(COLORS[pixel_idle_color])

if __name__ == '__main__':    
    keyboard.go()
