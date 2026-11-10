import numpy as np
import os
import pandas as pd

#Find the dataset in the same folder as this file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'B737_test.csv', 'B737_test.csv')

#Tracks overall max altitude and cruise speed totals across all chunks
max_alt = -np.inf
total_cruise_speed = 0.0
cruise_count = 0

#Reads the 1.67 GB file in 50,000 row chunks to get results without crashing my computer
for chunk in pd.read_csv(file_path, chunksize= 50000):
    data = chunk.to_numpy()
    altitude = data[:,7]
    velocity = data[:,10]
    cruise_speeds = velocity[altitude > 9144]

    #Updates max altitude while ignoring missing (NaN) values
    chunk_max = np.nanmax(altitude)
    if chunk_max > max_alt:
        max_alt = chunk_max

    #Adds valid cruise speeds to the running total
    valid_speeds = cruise_speeds[~np.isnan(cruise_speeds)]
    total_cruise_speed += np.sum(valid_speeds)
    cruise_count += len(valid_speeds)

#Calculates overall average cruise speed
avg_velocity = total_cruise_speed / cruise_count if cruise_count > 0 else 0

print(f'Maximum Altitude: {max_alt * 3.28084:.2f} feet')
print(f'Average Cruise Velocity: {avg_velocity * 2.23694:.2f} Mph')
