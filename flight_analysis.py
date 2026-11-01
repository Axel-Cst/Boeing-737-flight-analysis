import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'B737_test.csv', 'B737_test.csv')
data = np.genfromtxt(file_path, delimiter=',', skip_header=1, max_rows = 50000)

altitude = data[:,7]
velocity = data[:,10]
cruise_speeds = velocity[altitude > 9144]

max_alt = np.max(altitude)
avg_v = np.mean(cruise_speeds)

print(f'Maximum Altitude: {max_alt * 3.28084:.2f} feet')
print(f'Average Cruise Velocity: {avg_v * 2.23694:.2f} Mph')
np.save('b737_clean.npy', data)