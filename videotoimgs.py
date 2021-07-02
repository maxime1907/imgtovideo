import os
import cv2
import sys

def extract_frames(filepath, create_folder=True):
    if create_folder:
        try:
            os.mkdir(output_path)
        except:
            pass

    output_path = "{}.frames".format(filepath)
    vidcap = cv2.VideoCapture(filepath)
    frame_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_max_zero_size = len(str(frame_length))
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("{}/frame_{:0{len}d}.png".format(output_path, count, len=frame_max_zero_size), image)
        success,image = vidcap.read()
        count += 1

def extract_video_directory_as_frames(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=True):
        for name in sorted(files):
            filepath = os.path.join(root, name)
            print("Processing {}".format(filepath))
            extract_frames(filepath)
            print("Done")
        break

if __name__ == "__main__":
    for nb in range(1, len(sys.argv)):
        extract_video_directory_as_frames(sys.argv[nb])