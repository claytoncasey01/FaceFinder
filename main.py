from FaceDetector import FaceDetector
import sys
import os

# Get directory to search
rootdir = sys.argv[1]
fd = FaceDetector()

extract = False


# Check to see if a second argument
# was entered, if so see if it was
# the extract flag
if len(sys.argv) > 2:
    if sys.argv[2].lower() == "--extract":
        extract = True


# List of extensions so search for
extensions = ["jpg", "png", "gif", "jpeg"]

# Loop through all directories and subdirectories
# in the path entered
for subdir, dirs, files in os.walk(rootdir):
    # Loop through all files
    for f in files:
        # Check if they are images
        for extension in extensions:
            if extension in f:
                detected = fd.detect(os.path.join(subdir, f), extract)

                if not detected or extract:
                    os.remove(os.path.join(subdir, f))
