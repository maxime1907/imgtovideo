import cv2
import numpy as np
import glob
import sys

def image_sequences_to_video(dir_path, framerate=23.976):
    img_array = []
    frames_regex = '{}/*.png'.format(dir_path)
    for filename in sorted(glob.glob(frames_regex)):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('video.avi', 0, framerate, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        image_sequences_to_video(sys.argv[1], float(sys.argv[2]))
    else:
        print("Filepath, Framerate")