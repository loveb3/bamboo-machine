import cv2

def check_camera_access():
    camera_index = 0  # Change this index if needed (0, 1, 2, etc.)
    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        print(f"Unable to access camera at index {camera_index}")
    else:
        print(f"Camera access granted for index {camera_index}")

    camera.release()

if __name__ == "__main__":
    check_camera_access()
