# import os
#
# import cv2
#
# FACE_DETECTOR_PATH = "/usr/local/Caskroom/miniconda/base/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml"
#
#
# def crop_face(img, target_size=(480, 640), debug=False,
#               scaleFactor=1.25,
#               face_detector_path=FACE_DETECTOR_PATH):
#     face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor, 5)
#     max_y, max_x = img.shape[:2]  # get maximum image coordinates
#     tgt_width, tgt_height = target_size  # set target width & height
#     if len(faces) == 0:
#         return None
#     x, y, w, h = faces[0]  # consider only the first face that was found
#     delta_x, delta_y = (tgt_width - w) // 2, (tgt_height - h) // 2
#     x0, x1 = max(0, x - delta_x), min(x + w + delta_x, max_x)
#     y0, y1 = max(0, y - delta_y), min(y + h + delta_y, max_y)
#     if debug:
#         print(f"x0:\t{x0}\ty0:\t{y0}")
#         print(f"x1:\t{x1}\ty1:\t{y1}")
#     return img[y0:y1, x0:x1]
# # 480 640
#
# photos_dir = './faces'
# cropped_dir = './cropped_faces'
# for photo in os.listdir(photos_dir):
#     photo_path = os.path.join(photos_dir,photo)
#     img = cv2.imread(photo_path)
#     face = crop_face(img, img.shape[:2])
#     face = cv2.resize(face, (480,640))
#     # cv2.imshow('new', face)
#     cv2.imwrite(os.path.join(cropped_dir,photo), face)

from PIL import Image


def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))


if __name__ == '__main__':
    scale_image(input_image_path='./faces/glasses.jpeg',
                output_image_path='!tesssssst.jpg',
                width=480, height=640)