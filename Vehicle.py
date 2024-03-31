import cv2
import numpy as np


#Web camera
# Creates a VideoCapture object named cap to capture video frames.
cap=cv2.VideoCapture("video.mp4")

#Initialize Substractor

'''
The line you provided creates an instance of the background subtractor 
using the MOG (Mixture of Gaussians) algorithm in OpenCV.

cv2.bgsegm:This is a submodule in OpenCV that contains background segmentation algorithms.
createBackgroundSubtractorMOG(): This function creates an instance of the BackgroundSubtractorMOG class,
which is a background subtraction algorithm based on a mixture of Gaussians. This algorithm is commonly
used for motion detection and object tracking in computer vision applications.
'''

algo=cv2.createBackgroundSubtractorMOG2()

count_line_position=550

min_width_rect=80 #min width rectangle

min_height_rect=80 #min height rectangle

#This finction is for finding the middle point of rectangle
def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy

detect=[]

offset=6 #Allowable error between pixel

counter=0


while True:
    '''
    Reads a frame from the video capture (cap) and stores it in the variables ret and frame1.
    ret is a boolean variable indicating whether the frame was read successfully.
    '''
    ret,frame1=cap.read()
    #cv2.cvtColor: This is a function in OpenCV used for color space conversion. 
    #It converts an input image from one color space to another.
    #cv2.COLOR_BGR2GRAY: This is the color space conversion code specifying that the conversion should be from BGR to grayscale. 
    #Grayscale images have only one channel, representing the intensity or brightness of each pixel, instead of three channels 
    #for color images.
    '''
    grey will contain the grayscale version of the original color frame (frame1). Grayscale images are often used in computer vision
    applications because they require less computational resources compared to color images, and they simplify certain image processing
    tasks such as edge detection and object recognition.
    '''
    grey=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    #cv2.GaussianBlur: This is a function in OpenCV that applies a Gaussian blur to an image. Gaussian blur is a common image smoothing technique.
    #(3, 3): This is the kernel size of the Gaussian filter.
    #5: This is the standard deviation of the Gaussian kernel along the X and Y directions. 
    #After this line, the variable blur will contain the grayscale image (grey) with Gaussian blur applied.
    blur=cv2.GaussianBlur(grey,(3,3),5)



    #applying on each frame 

    img_sub=algo.apply(blur)

    #cv2.dilate() is a morphological operation in OpenCV that is used to enhance features in an image.
    #It is particularly useful for tasks such as increasing the size of foreground objects, closing small gaps in contours, and connecting nearby contours.
    #dilate=cv2.dilate(img_sub,np.ones((5,5)))

    #kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

    #dilatada=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
    # Alternatively, create an elliptical structuring element
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # Perform closing operation using cv2.morphologyEx() with MORPH_CLOSE
    dilated_image_morph = cv2.morphologyEx(img_sub, cv2.MORPH_CLOSE, kernel)
    
    dilated_image_morph = cv2.morphologyEx(dilated_image_morph, cv2.MORPH_CLOSE, kernel)
    
    #used to find contours in a binary image. Contours are simply the boundaries of objects in an image, and 
    #they are represented as lists of points.
    counterShape,h=cv2.findContours(dilated_image_morph,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
     
    # start -> (25,550) end-> (1200,550)
    cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)
    
    #drawing rectangle in each vehicle
    for (i,c) in enumerate(counterShape):
        (x,y,w,h)=cv2.boundingRect(c)
        validate_counter=(w>=min_width_rect) and (h>=min_height_rect)
        if not validate_counter:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)

        center=center_handle(x,y,w,h)
        #Detect will count the number of vehicle
        detect.append(center)
        
        #Creates a red circle on the center of rectangle
        cv2.circle(frame1,center,4,(0,0,255),-1)

        for (x,y) in detect:
            if y<(count_line_position+offset) and y>(count_line_position-offset):
                counter=counter+1 
                #change the counter line color when touching
                cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(0,127,255),3)
                detect.remove((x,y))
                print("Vehicle Counter:",str(counter))
            
            cv2.putText(frame1,"Vehicle Counter :"+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)

            

    # Displays the current frame (frame1) in a window named 'video Orginal'.
    cv2.imshow('video Orginal',frame1)

    '''
    Waits for a key event. If the key pressed is the Enter key (13 in ASCII),
    it breaks out of the loop, effectively stopping the video capture.
    '''
    if cv2.waitKey(1)==13:
        break

#Closes all OpenCV windows
cv2.destroyAllWindows()
#Releases the video capture object (cap)
cap.release()



