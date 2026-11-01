import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'B737_test.csv', 'B737_test.csv')

try:
    with open(file_path, 'r') as file:
        print('--- FIRST 5 LINES OF THE DATASET ---')
        for i in range(5):
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("Could not find the file.")