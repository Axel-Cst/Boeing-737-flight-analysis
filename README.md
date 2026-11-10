# Boeing 737 Flight Analysis Project

I built this Python tool using **Pandas** and **NumPy** to process and analyze a 1.67 GB dataset of Boeing 737 flight telemetry. Because loading a file that large would exceed my computer's 4 GB RAM limit and freeze vs code, I wrote my code so it would analyze the whole dataset in chunks  of 50,000 rows.

## How the Code works

* **Chunked Streaming ('flight_analysis.py'):** Uses 'pandas.read_csv()' with 'chunksize=50000' to read 50,000 rows at a time, converting each piece into a NumPy array so it never overloads my computer's memory.
* **Portable File Paths:** Uses Python's 'os' library to build a relative file path so the script can run on any computer without breaking.
* **Cruise Filtering & Math:** Uses a NumPy boolean masking ('altitude > 9144') to filter out slow takeoff and landing data, ignores missing ('NaN') values, and tracks running totals across every chunk to get the exact average.
  
  ## What the Data showed Me
* **Maximum Altitude Reached:** 41,175.00 feet (this matches the real-world maximum ceiling limit a real Boeing 737 can fly)
* **Average Cruise Speed:** 507.24 MPH

## Tools used
* Python 3
* Pandas (chunked CSV streaming)
* NumPy (boolean masking, NaN filtering, and array math)
* OS Standard Library
