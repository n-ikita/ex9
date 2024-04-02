class TrafficLight:
    permissible_values = ['green', 'yellow', 'red', 'yellow']

    def __init__(self):
        self.current_signal = 0

    def next_signal(self):
        self.current_signal = (self.current_signal + 1) % len(TrafficLight.permissible_values)

    def get_signal(self):
        return TrafficLight.permissible_values[self.current_signal]

    def __repr__(self):
        return f'signal: {TrafficLight.permissible_values[self.current_signal]}'


trafficLight = TrafficLight()
for _ in range(10):
    print(trafficLight)
    trafficLight.next_signal()
