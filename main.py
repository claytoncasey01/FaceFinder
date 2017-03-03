from FaceDetector import FaceDetector
import argparse
import os
import json
import sys

# Create our arg parser and parse arguments
ap = argparse.ArgumentParser()

ap.add_argument("-rd", "--root-dir", required=True,
                help="Root directory to begin searching. Will go through all subdirectories searching for images")
ap.add_argument("-e", action="store_true", required=False,
                help="Detect and extract faces from images all in one go.")
ap.add_argument("-ch", "--config-haar", required=False,
                help="Configures location of haar cascade.")

args = vars(ap.parse_args())

# Get directory to search
rootdir = args["root_dir"]
fd = FaceDetector()

# Configure path of haar classifier
if args["config_haar"] is not None:
    print(args["config_haar"])
    with open("config.json", "w") as f:
        config_dict = {"haar_path": args["config_haar"]}
        json.dump(config_dict, f)

# List of extensions so search for
extensions = ["jpg", "png", "gif", "jpeg"]

# Output to indicate program
# is running.
print("[X] Working...")

# Loop through all directories and subdirectories
# in the path entered
for subdir, dirs, files in os.walk(rootdir):
    # Loop through all files
    for f in files:
        # Check if they are images
        for extension in extensions:
            if extension in f:
                # Attempt to load our config file with haar classifier
                # path and throw exception if not found.
                try:
                    haar = open("./config.json", "r")
                    haar = json.load(haar)
                    detected = fd.detect(os.path.join(subdir, f), args["e"], haar["haar_path"])
                except (OSError, IOError):
                    sys.exit("[X] Error: Could not find config.json, please run again with --config-haar flag.")

                if not detected or args["e"]:
                    os.remove(os.path.join(subdir, f))
