# Face Recognition Using OpenCV and Face_Recognition Library

## Introduction
This project is a simple face recognition system implemented using OpenCV and the face_recognition library. The system allows real-time face recognition from a webcam feed, comparing detected faces with known faces stored in a directory. When a known face is detected, the system will display the name associated with that face in a bounding box.

## Requirements
To run this project, you need the following:

1. Python (version 3.6 or higher)
2. OpenCV library (`cv2`)
3. NumPy library (`numpy`)
4. face_recognition library (`face_recognition`)

You can install the required libraries using pip:

```bash
pip install opencv-python numpy face_recognition
```

## How to Use

1. Clone the repository or download the project files.

2. Prepare the "Faces" directory:

   - Create a folder named "Faces" in the same directory as the Python script.
   - Add images of known faces to the "Faces" folder. Make sure each image contains only one face, and the filename represents the name of the person (e.g., "john.jpg" for John's image).

3. Run the script:

   Open your terminal or command prompt and navigate to the project directory. Then, execute the following command:

   ```python
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of the Python script containing the provided code.

4. The webcam feed will open, and the face recognition system will start detecting faces in real-time.

## How It Works

1. The script loads images from the "Faces" directory and encodes them using the `encodeImg` function. The face_encodings function from the `face_recognition` library extracts facial features from each image and converts them into a 128-dimensional vector.

2. The webcam feed captures frames continuously. Each frame is resized and converted to RGB format for compatibility with the `face_recognition` library.

3. The `face_recognition` library is used to detect faces in the resized frame and encode them.

4. For each detected face in the frame, the system compares the encoded face with the encoded faces from the "Faces" directory using the `compare_faces` function from the `face_recognition` library.

5. If a match is found, the system retrieves the associated name and displays it in a bounding box around the recognized face.

6. The process continues in real-time, allowing continuous face recognition from the webcam feed.

## Important Note

Please note that this is a basic face recognition system meant for educational purposes. In real-world applications, more advanced techniques and precautions should be used to enhance security and handle various scenarios. For instance, handling multiple faces in a single frame, dealing with changes in lighting conditions, and ensuring the privacy and security of the recognized individuals.

## Disclaimer

This project is solely for educational and learning purposes. Use the system responsibly and respect the privacy and rights of others. The developers of this project are not responsible for any misuse or unethical use of the system.

## Conclusion

Congratulations! You have successfully set up and run a simple face recognition system using OpenCV and the face_recognition library. Feel free to experiment and improve the project, exploring more advanced techniques to make the system more robust and accurate. Happy coding!
