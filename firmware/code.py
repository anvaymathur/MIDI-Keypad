import microcontroller
import touchio
import usb_midi
import adafruit_midi
import rotaryio
import neopixel
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

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
            midi.send(NoteOn(NOTES[i] + octave * 12, 100))
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