from OpenEZ import *
camera = cameraSelector(0, DSHOW) 

while camera.isOpened():
    ret, frame = camera.read()
    waitKey(10) 
    
    show("Camera", frame)