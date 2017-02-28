import cv2


class FaceDetector:

    # Searches for face in image
    def detect(self, path):
        img = cv2.imread(path)

        cascade = cv2.CascadeClassifier("/home/casey/FaceFinder/haarcascade_frontalface_alt.xml")
        faces = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))

        self.extract_faces(img, faces)

        # Check if we found any faces
        if len(faces) == 0:
            return False

            # if self.crop_faces:
            #   print("Made it")
            #   self.extract_faces(img, faces)

        return True

    def extract_faces(self, img, faces):
        print("Here")
        for f in faces:
            x, y, w, h = [v for v in f]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255))

            sub_face = img[y:y + h, x:x + w]
            face_file_name = "ace_" + str(y) + ".jpg"
            cv2.imwrite(face_file_name, sub_face)

        cv2.imshow("Window", img)

        return
