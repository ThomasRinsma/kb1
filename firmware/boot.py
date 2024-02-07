import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP26,  # column for Esc
    source=board.GP15, # row for Esc
    midi=False,
    mouse=False,
    storage=True, # set to False to only mount when Esc is held during bootup
    usb_id=('Th0mas', 'th0mas.nl - kb1 - v1'),
)