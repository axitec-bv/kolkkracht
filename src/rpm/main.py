#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import argparse

# Constants
SENSOR_PIN = 17  # BCM pin number for the sensor input
pulse_count = 0  # Global pulse counter

def rpm_callback(channel):
    """Callback function triggered on rising edge detection."""
    global pulse_count
    pulse_count += 1

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Measure RPM using a sensor on GPIO pin."
    )
    parser.add_argument(
        "--interval", "-i",
        type=float,
        default=5.0,
        help="Measurement interval in seconds (default: 5.0)"
    )
    args = parser.parse_args()
    
    interval = args.interval

    # Configure GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=rpm_callback, bouncetime=5)

    print(f"Starting RPM measurement every {interval} second(s). Press CTRL+C to exit.")

    try:
        while True:
            time.sleep(interval)
            
            # Because there are 4 holes per revolution:
            #   revolutions = pulse_count / 4
            #   rpm = revolutions * (60 / interval) = (pulse_count / 4) * (60 / interval)
            global pulse_count
            revolutions = pulse_count / 4.0
            rpm = revolutions * (60.0 / interval)
            print(f"RPM: {rpm:.2f}")
            
            # Reset pulse counter for the next interval
            pulse_count = 0
    
    except KeyboardInterrupt:
        print("\nMeasurement stopped by user.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
