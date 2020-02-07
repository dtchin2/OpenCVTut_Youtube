import cv2

video_name = 'myfile.avi'
cap = cv2.VideoCapture(0)  # is the device number... default is 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_name, fourcc, 20.0, (640, 480))  # takes name of output file

print(cap.isOpened())

while cap.isOpened():
    # infinite loop, capture the frames
    ret, frame = cap.read()

    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# once the loop is complete release resources
cap.release()
out.release()
cv2.destroyAllWindows()

