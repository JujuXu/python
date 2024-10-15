#numpy         2.1.2
#opencv-python 4.10.0.84
#pip           24.2

import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0) # open webcam

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250) # load aruco dictionary

params = aruco.DetectorParameters() # import parameters for detector

detector = aruco.ArucoDetector(aruco_dict, params) # create aruco detector

while True:
    valid, frame = cap.read() # valid is boolean set if frame got, frame is one frame of video

    if valid:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert frame in gray

        corners, ids, rejected = detector.detectMarkers(gray) # detect markers from gray frame

        if ids is not None:
            
            aruco.drawDetectedMarkers(frame, corners, ids) # draw aruco markers surroundings

            print("IDs DETECTED:")
            # display detected aruco markers
            for i, corner in zip(ids, corners):
                
                center = corner[0].mean(axis=0).astype(int) # compute aruco marker centers
                
                cv2.putText(frame, str(i[0]), tuple(center), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA) # put ID text on frame
                print("> "+str(i[0]))
        cv2.imshow('Aruco Visualisation', frame) # display frame

    # pressing this key exits the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # release the webcam, close it to be opened by other apps
cv2.destroyAllWindows() # close windows from cv2