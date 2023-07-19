import cv2 as cv

# Reading an image and displaying it

# cat = cv.imread('./Photos/cat_large.jpg')
# cv.imshow('Cat', cat)

# cv.waitKey(0)

# Reading videos

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/kitten.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', rescaleFrame(frame, .2))
    cv.imshow('R 1', rescaleFrame(frame, .4))
    cv.imshow('R 2', rescaleFrame(frame, .6))
    cv.imshow('R 3', rescaleFrame(frame, .8))
    

    if cv.waitKey(20) & 0xFF == ord('d') :
        break

capture.release()
cv.destroyAllWindows()