from FaceDetector import FaceDetector
import sys
import os

# Get directory to search
rootdir = sys.argv[1]
fd = FaceDetector()

# Loop through all directories and subdirectories
# in the path entered
for subdir, dirs, files in os.walk(rootdir):
    # Loop through all files
    for f in files:
        # Check if they are images
        if ".jpg" in f:

            try:
                detected = fd.detect(os.path.join(subdir, f))
                os.remove(os.path.join(subdir, f))

            except:
                print("Error on file" + os.path.join(subdir, f) + " removing...")
                os.remove(os.path.join(subdir, f))
