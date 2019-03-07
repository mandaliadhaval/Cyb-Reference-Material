from PIL import Image

import face_recognition_models

import face_recognition

import os



image = face_recognition.load_image_file("image2.jpg")


face_locations = face_recognition.face_locations(image)

i = 0

print('Total found faces are', len(face_locations))

for face_location in face_locations:

        # Print the location of each face in this image

    top, right, bottom, left = face_location

    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,

                                                                                                    right))



        # You can access the actual face itself like this:

    face_image = image[top:bottom, left:right]

    pil_image = Image.fromarray(face_image)

    pil_image.show()

    print('Saving image {}'.format(i))

    pil_image.save('{}.jpg'.format(i))

    i = i + 1
