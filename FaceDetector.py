import cv2


class FaceDetector:

    # Searches for face in image
    def detect(self, path, extract):

        # Attempt to read the image and find
        # the faces.
        try:
            img = cv2.imread(path)
            cascade = cv2.CascadeClassifier("/home/casey/FaceFinder/haarcascade_frontalface_alt.xml")
            faces = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))

            # If extract flag was passed in
            # then extract the faces from
            # the image.
            if extract:
                self.extract_faces(img, faces, path)
        except:
            return False

        # Check if we found any faces
        if len(faces) == 0:
            return False

        return True

    def extract_faces(self, img, faces, path):
        for f in faces:
            x, y, w, h = [v for v in f]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255))

            sub_face = img[y:y + h, x:x + w]
            face_file_name = path + "face_" + str(y) + ".jpg"
            cv2.imwrite(face_file_name, sub_face)

        return

    def match_faces(self, path, template, threshold=0.60):
        matched = False
        img = cv2.imread(path, 0)
        template = cv2.imread(template, 0)
        w, h = template.shape[::-1]
        method = cv2.TM_CCOEFF_NORMED

        # Apply template matching
        res = cv2.matchTemplate(img, template, method)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if our max value is >=
        # the threshold passed in(default of .60)
        if max_val >= threshold:
            matched = True

        return matched



