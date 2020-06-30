import cv2 ,time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#importing the Face Cascade XML file into the Application which has all the features of a human face
smile_cascade = cv2.CascadeClassifier("smile.xml")
#importing the Smile Cascade XML file into the Application which has all the features of a human smile
video=cv2.VideoCapture(0)

while True:
    #we'll be needing an iinfinet loop so that we can capture the picture continously to make it look like an video 
    check,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #converting the coloured image into the gray image using the cvtColor function
    
    #Recogination in a GRAY picture is much accurate as compared to the Coloured Image
    face = face_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 5)
    #here we are doing the face recogonation and inside this face recogination we'll do the smile recogination 
    for x,y,w,h in face:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0, 255 ,0), 3) 
        smile = smile_cascade.detectMultiScale(gray,scaleFactor = 1.5, minNeighbors = 20)
        #doing the smile recogination 
        for x,y,w,h in smile:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255 , 0, 0), 3)

    cv2.imshow('gotcha',frame)
    key=cv2.waitKey(1)

    if key == ord(' '):# here we have used a space_bar to terminate the window
         break

video.release()
# to release the video that we have created i.e the images that we have been capturing through our web_cam
cv2.destroyAllWindows        
#to destroy all the windows opened in the cv module
