from machine import Pin
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_fast():
    wrap_target()
    set(pins, 1)
    set(pins, 0)
    wrap()

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_1hz():
    set(pins, 1)
    set(x, 7)                  
    label("delay_high")
    nop()                       [29]
    jmp(x_dec, "delay_high")

    set(pins, 0)
    set(x, 31)                  
    label("delay_low")
    nop()                       [29]
    jmp(x_dec, "delay_low")

#machine.freq(250000000);

sm0 = rp2.StateMachine(0, blink_fast, freq=60000000, set_base=Pin(15)) # ca clignote à 30Mhz !
sm0.active(1)



sm1 = rp2.StateMachine(1, blink_1hz, freq=2000, set_base=Pin(25))
sm1.active(1)
