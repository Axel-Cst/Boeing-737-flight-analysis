import numpy as np

data = np.load('b737_clean.npy')

altitude = data[:,7]
velocity = data[:,10]

max_alt = np.max(altitude)
cruise_speeds = velocity[altitude > 9144]
avg_cs = np.mean(cruise_speeds)

print(f"Max altitude: {max_alt * 3.28084:.2f} feet")
print(f"Average cruise speed: {avg_cs * 2.23694:.2f} mph")