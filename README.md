# Boeing 737 Flight Analysis Project

I built this Python tool using **NumPy** to clean up and analyze a huge 1.67 GB dataset of Boeing 737 flight tracking numbers. Because the raw text file was so massive, it kept freezing up my text editors when I tried to open it. I had to design a smart way to break down the file and process the numbers efficiently without overloading my computer's memory

## How the Code works

* **Step 1: looking at the Data ('explore.py')**
 I started by writing a tiny script to open the file and print just the first 5 lines. This helped me find the column layout and see       exactly where the altitude and velociy numbers were sitting without loading the giant file
* **Step 2: Cleaning and Streaming ('flight_analysis.py')**
 Instead of importing everything at once, this script streams a safe chunk of 50,000 rows. I used Python's 'os' library to build a         relative file path so the code can run on any computer without breaking. At the end of the script, I used 'np.save()' to freeze our       clean numbers into a raw binary format ('.npy').
* **Step 3: Instant Analytics ('fast_analysis.py')**
 Repetitive text processing takes forever, so this script uses 'np.load()' to open our pre-made binary file instantly. To find the true    cruise performance of the planes, I used a NumPy boolean mask ('altitude > 9144') to instantly filter out the slow takeoff and landing    data, leaving me with only high-altitude flight metrics.
  
  ## What the Data showed Me
* **Maximum Altitude Reached:** 41,175.00 feet (this matches the real-world maximum ceiling limit a real Boeing 737 can fly)
* **Average Cruise Speed:** 510.12 MPH

## Tools used
* Python 3
* NumPy (vectorized slicing & Math Functions), OS Standard Library
