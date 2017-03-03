from FaceDetector import FaceDetector
import argparse
import os

# Create our arg parser and parse arguments
ap = argparse.ArgumentParser()

ap.add_argument("-d", "--root-dir", required=True,
                help="Root directory to begin searching. Will go through all subdirectories searching for images")
ap.add_argument("-e", action="store_true", required=False,
                help="Detect and extract faces from images all in one go.")

args = vars(ap.parse_args())

# Get directory to search
rootdir = args["root-dir"]
fd = FaceDetector()

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
                detected = fd.detect(os.path.join(subdir, f), args["e"])

                if not detected or args["e"]:
                    os.remove(os.path.join(subdir, f))
