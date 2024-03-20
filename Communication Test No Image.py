import serial
import cv2

# Serial port settings
SERIAL_PORT = 'COM7'  # Change this to match your Arduino's serial port
BAUD_RATE = 9600

# Function to capture image from USB camera
def capture_image():
    print("Image signal received")

# Main function
def main():
    # Open serial port
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Serial port {SERIAL_PORT} opened successfully.")
    except serial.SerialException as e:
        print(f"Failed to open serial port {SERIAL_PORT}: {e}")
        return

    # Main loop
    while True:
        try:
            # Read a single character from serial
            data = ser.read().decode('utf-8')

            # If 'P' is received, capture an image
            if data == 'P':
                capture_image()

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Exiting program.")
            break

        except Exception as e:
            print(f"Error: {e}")

    # Close serial port
    ser.close()
    print("Serial port closed.")

if __name__ == "__main__":
    main()
