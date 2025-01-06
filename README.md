# Object Detection by Color (Red, Green, Blue)  

This project uses Python and OpenCV to detect and count objects of specific colors (red, green, and blue) in real-time using a webcam feed. The program identifies objects based on their HSV color range, draws bounding boxes around them, and displays the total count of detected objects for each color.

## Features  
- Detects red, green, and blue objects in real-time using a webcam.  
- Draws bounding boxes and marks the center of detected objects.  
- Displays the total count of objects for each color on the video feed.  

## Prerequisites  
Ensure the following are installed on your system:  
- Python 3.x  
- OpenCV  
- NumPy  

## Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/Object-Detection-by-Color.git  

2. Navigate to the project directory :
   cd Object-Detection-by-Color

3. Install the required libraries:
   pip install opencv-python numpy

4. How to Run :
   (1). Open a terminal and navigate to the project directory.
   (2). Run the Python script:
           python color_detection.py  
   (3). The webcam feed will open in a new window. Detected objects will be marked with bounding boxes, and their counts will be displayed on the video feed.
   (4). Press the Esc key to close the window and stop the program.

5. Code Explanation
   - HSV Color Range
        The program uses the HSV color space to detect specific color ranges:
        Red: [126,188,47] to [179,255,255]
        Green: [66,155,40] to [98,255,255]
        Blue: [88,176,70] to [133,255,255]

   - Object Detection
        For each color:
        The program creates a mask to isolate the color.
        Contours are extracted from the mask.
        Objects with an area greater than a threshold (600) are considered valid detections.

   - Output
       Bounding boxes and centers of detected objects are marked on the video feed.
       Total counts for each color are displayed on the screen.

6. Customization :
   - Adjust HSV Ranges:
       Modify the red_LR, red_UR, green_LR, green_UR, blue_LR, and blue_UR variables to detect different shades of red, green, or blue.
   - Change Area Threshold:
       Update the value of x in the functions (red, green, blue) to adjust the minimum size of objects to be detected.

     
8. Example Output :
     The program will display a webcam feed with bounding boxes around detected objects, like this:
         Total Red objects : 2  
         Total Green objects : 1  
         Total Blue objects : 3

9. License :
    This project is licensed under the MIT License.

10. Contact :
    For any questions or suggestions, feel free to reach out:
    Email: patelparam057@gmail.com
    GitHub: Param5241
