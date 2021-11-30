import glob
from pathlib import Path
from PIL import Image
import cv2
import numpy as np
import os


def video_to_images(save_path: Path, video_path='inference/test_video.mp4'):
    """Convert video frames into images"""

    vidcap = cv2.VideoCapture(video_path)
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        if success:
            cv2.imwrite(f'{save_path / f"{count}.png"}', image)
            count += 1
            print(f'number of images: {count}...', end='\r')
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()


def image_list_to_video(fname, image_path: Path):

    images = image_path.glob("*.png")
    images = sorted(images, key=lambda x: int(os.path.basename(x).split('.')[0]))
    height, width, _c = np.array(Image.open(images[0])).shape

    out = cv2.VideoWriter(fname, cv2.VideoWriter_fourcc(*'DIVX'), 15, (width, height))
    for img_fp in images:
        img = cv2.imread(str(img_fp))
        out.write(img)
    out.release()


def main():

    video_frame_path = Path('inference/helmet-vid-frames')
    if not os.path.exists(video_frame_path):
        video_frame_path.mkdir()
        video_to_images(video_frame_path)

    if not os.path.exists('inference/helmet-vid-results'):
        print(f'please run ')
    else:
        image_list_to_video(fname='inference/test-results.avi',
                            image_path=Path('inference/helmet-vid-results'))


if __name__ == "__main__":
    main()
