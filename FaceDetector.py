import cv2

class FaceDetector:

    # Searches for face in image
    def detect(self, path):
        img = cv2.imread(path)

        cascade = cv2.CascadeClassifier("/home/casey/FaceFinder/haarcascade_frontalface_alt.xml")
        rects = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))

        # Check if we found any faces
        if len(rects) == 0:
            return False

        return True
