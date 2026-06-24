# Muthuramcodes
# Interactive Robot Dog

An Arduino-based robotic pet that combines:

- OLED eye animations
- Tail wagging servo
- Front obstacle detection
- Side proximity sensing
- Line following
- Push-button diagnostics mode

## Components

- Arduino Uno
- L298N Motor Driver
- SSD1306 OLED Display
- SG90 Servo
- HC-SR04 Ultrasonic Sensors (x3)
- IR Line Sensors (x2)
- DC Motors

## Features

### Object Tracking
The robot detects nearby objects using ultrasonic sensors and follows them.

### Line Following
When no object is detected, the robot follows a black line using IR sensors.

### Emotional Display
OLED eyes open while active and blink while idle.

### Tail Animation
The servo simulates a wagging tail whenever the robot is moving.

## Future Improvements

- Voice commands
- Bluetooth control
- Facial recognition
- Mobile app integration
