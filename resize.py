import cv2 as cv

capture = cv.VideoCapture('./Videos/kitten.mp4')

def resize(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    


while 1:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resize(frame))

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()