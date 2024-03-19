import csv
import datetime
import serial


SERIAL_PORT = 'COM3'

BAUD_RATE = 9600


ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

def get_probe_data():
    line = ser.readline().decode('utf-8').strip()
    print(f"Received from serial: '{line}'")
    try:

        parts = line.split(', ')
        if len(parts) == 3:
            x_str, radius_str, angle_str = parts
            x_position = float(x_str.split(': ')[1])
            radius = float(radius_str.split(': ')[1])
            angle = float(angle_str.split(': ')[1])
            return x_position, radius, angle
        else:
            print("Error: Unexpected data format")
            return None, None, None
    except ValueError as e:
        print(f"Error processing line '{line}': {e}")
        return None, None, None



with open('sensor_data_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["X Position", "Radius", "Angle"])

    data_point_limit = 50  # for example, stop after 100 data points
    data_points_collected = 0

    while data_points_collected < data_point_limit:
        x_position, radius, angle = get_probe_data()

        if x_position is not None and radius is not None and angle is not None:
            writer.writerow([x_position, radius, angle])
        else:
            print("No valid data received for this entry")
        # Break the loop or add a condition to stop data collection as needed
        data_points_collected += 1


ser.close()
print("Data saved to sensor_data_test.csv")