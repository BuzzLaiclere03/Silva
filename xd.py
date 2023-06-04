#!/usr/bin/env python
import time
import pigpio

I2C_ADDR=0x69

def i2c(id, tick):
    global pi

    s, b, d = pi.bsc_i2c(I2C_ADDR)
    response_data = [0x24, 
                         1, 
                         2, 
                         3, 
                         4, 
                         5, 
                         6,
                         7, 
                         8,
                         9]  # Change this with your response data

    if b:
        s, b, d = pi.bsc_i2c(I2C_ADDR, response_data)

pi = pigpio.pi()

if not pi.connected:
    exit()

# Respond to BSC slave activity

pi.set_pull_up_down(10, pigpio.PUD_UP)
pi.set_pull_up_down(11, pigpio.PUD_UP)

e = pi.event_callback(pigpio.EVENT_BSC, i2c)

pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

time.sleep(600)

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral

pi.stop()