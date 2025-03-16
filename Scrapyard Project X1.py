
import time
import random  # Simulating sensor readings since we don't have real hardware

# Simulate GPIO Pins (since we're not on actual hardware)
class Pin:
    def __init__(self, pin, direction):
        self.pin = pin
        self.direction = direction
        self.value_state = 0
        
    def high(self):
        self.value_state = 1
        print(f"Pin {self.pin} set to HIGH")
        
    def low(self):
        self.value_state = 0
        print(f"Pin {self.pin} set to LOW")
        
    def value(self):
        return random.choice([0, 1])  # Simulate readings

# Define GPIO Pins (simulated)
TRIG_PIN = Pin(3, "OUT")
ECHO_PIN = Pin(2, "IN")
LED = Pin(5, "OUT")
BUZZER = Pin(6, "OUT")

# Simulate object movement
class ObjectSimulator:
    def __init__(self):
        self.distance = random.uniform(15, 35)  # Random starting distance
        self.moving = True
        self.base_speed = 1.0  # Increased base speed
        self.movement_intensity = random.uniform(1, 3)
        self.direction = random.choice([-1, 1])
        
    def update(self):
        # More frequent movement changes
        if random.random() < 0.2:  # 20% chance to change movement
            self.direction = random.choice([-1, 1])
            self.movement_intensity = random.uniform(0.5, 5.0)  # More varied intensity
        
        # Update distance based on movement intensity
        if self.moving:
            move_speed = self.base_speed * self.movement_intensity
            self.distance += self.direction * move_speed
            self.distance = max(10, min(50, self.distance))  # Keep within bounds
            
        return round(self.distance, 1)

simulator = ObjectSimulator()

# Function to simulate distance measurement
def get_distance():
    TRIG_PIN.low()
    time.sleep(0.000002)  # 2 microseconds
    TRIG_PIN.high()
    time.sleep(0.00001)   # 10 microseconds
    TRIG_PIN.low()
    
    return simulator.update()

# Get initial position
initial_distance = get_distance()
print(f"Initial distance: {initial_distance:.1f} cm")

# Movement detection loop
while True:
    current_distance = get_distance()
    print(f"Current distance: {current_distance:.1f} cm")

    if abs(current_distance - initial_distance) > 3:
        print("⚠️ Movement detected! ⚠️")
        LED.high()
        BUZZER.high()
        time.sleep(0.5)
        LED.low()
        BUZZER.low()
    
    time.sleep(1)  # Wait a second before next reading
