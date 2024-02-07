# `kb1`: a fully DIY mechanical keyboard

_(WIP: I am slowly collecting stuff into this one repo. FW/HW will be added)_

![](pics/full_centered.jpg)

Features:

- Mechanically built using two PCBs and a few screws and standoffs.
- Proper "tenkeyless" layout, compatible with Cherry MX-style switches (mine with Kailh box crystal jades)
- Per-key RGB backlight using reverse-mounted SK6812 neopixels
- Featuring an old-school 16x2 character display
- An of course a _knob_ (rotary encoder)
- Based on the Raspberry Pi Pico and [KMK](https://github.com/KMKfw/kmk_firmware)

## Why?

To challenge myself and practice PCB design!

Is it tons of fun to design and build your own keyboard from scratch? Hell yeah. Would I recommend this board for daily use? Not really :^)

## Hardware / BoM

TODO


## Firmware

It's just a simple KMK setup with scaffolding code for the display and RGB. Actually doing something with the display is still TBD.

As a demo there is currently a bit of logic to map individual RGB leds to keys so it can light up a key when pressed. Twisting the knob changes the overall backlight color.

TODO: build/flash instructions.


## Pics

| | |
|:---:|:---:|
|![](pics/bottom.jpg)|![](pics/inside_pico.jpg)|
|![](pics/left_view.jpg)|![](pics/right_view.jpg)|
|![](pics/top_back_view.jpg)|![](pics/kb1.jpg)|


## Disclaimer 

This is my own hobby project and I'm a total PCB design newbie. Use the info and files provided here at your own risk.