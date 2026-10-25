import microcontroller
import touchio
import usb_midi
import adafruit_midi
import rotaryio
import neopixel
import busio
import displayio
import terminalio
import i2cdisplaybus
import adafruit_displayio_ssd1306
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_display_text  import label



displayio.release_displays()

PINS = [
    microcontroller.pin.GPIO1,
    microcontroller.pin.GPIO2,
    microcontroller.pin.GPIO3,
    microcontroller.pin.GPIO4,
    microcontroller.pin.GPIO5,
    microcontroller.pin.GPIO6,
    microcontroller.pin.GPIO7
]

NOTES = [60, 62, 64, 65, 67, 69, 71]

keys= [touchio.TouchIn(pin) for pin in PINS]

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)
was_touched = [False] * 7

encoder = rotaryio.IncrementalEncoder(
    microcontroller.pin.GPIO8, microcontroller.pin.GPIO9
)
last_position = encoder.position
octave = 0 

pixels = neopixel.NeoPixel(microcontroller.pin.GPIO10, 3, brightness=0.2)
lit = False

i2c = busio.I2C(scl=microcontroller.pin.GPIO44, sda=microcontroller.pin.GPIO43)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

screen = displayio.Group()
note_text = label.Label(
    terminalio.FONT,
    text="--",
    scale=4,
    anchor_point=(0.5, 0.5),
    anchored_position=(64, 32),
)
screen.append(note_text)
display.root_group = screen

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def note_name(n):
    return NOTE_NAMES[n % 12] + str(n // 12 - 1)

while True:
    position = encoder.position
    if position != last_position:
        for i in range(7):
            if was_touched[i]:
                midi.send(NoteOff(NOTES[i] + octave * 12, 0))
                was_touched[i] = False
        octave += position - last_position
        octave = max(-3, min(3, octave))
        last_position = position

    for i in range(7):
        touched = keys[i].value
        if touched and not was_touched [i]:
            note = NOTES[i] + octave * 12
            midi.send(NoteOn(note, 100))
            note_text.text = note_name(note)
        elif not touched and was_touched[i]:
            midi.send(NoteOff(NOTES[i] + octave * 12, 0))
        was_touched[i] = touched

    any_touched = True in was_touched
    if any_touched != lit:
        if any_touched:
            pixels.fill((0,120,255))
        else:   
            pixels.fill((0,0,0))
        lit = any_touched