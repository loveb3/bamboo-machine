import serial
import cv2

# Serial port settings
SERIAL_PORT = 'COM7'  # Change this to match your Arduino's serial port
BAUD_RATE = 9600


def main():


    try:
        # Open serial port
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Serial port {SERIAL_PORT} opened successfully.")

        # Main loop to continuously read data from serial
        while True:
            # Read a line of data from serial
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"Received data: {data}")

    except serial.SerialException as e:
        print(f"Failed to open serial port {SERIAL_PORT}: {e}")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Exiting program.")

    finally:
        # Close serial port
        if ser.is_open:
            ser.close()
            print("Serial port closed.")


if __name__ == "__main__":
    main()
