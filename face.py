from PIL import Image, ImageDraw
import face_recognition


def midpoint(coors):
    """
    get midpoint of coors
    :param coors:[(x, y), ...]
    :return:
    """
    x, y = 0, 0
    for coor in coors:
        x += coor[0]
        y += coor[1]
    x, y = int(x / len(coors)), int(y / len(coors))
    return x, y


if __name__ == '__main__':
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("face/trump-1.jpg")

    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    num_faces = len(face_landmarks_list)

    if num_faces == 1:
        # Create a PIL imagedraw object so we can draw on the picture
        pil_image = Image.fromarray(image)
        img_size = pil_image.size
        d = ImageDraw.Draw(pil_image)

        for face_landmarks in face_landmarks_list:
            for facial_feature in face_landmarks.keys():
                print("{} : {}".format(facial_feature, face_landmarks[facial_feature]))

        face_landmarks = face_landmarks_list[0]
        centre_nose_bridge = midpoint(face_landmarks['nose_bridge'])

        d.point(centre_nose_bridge, fill='blue')
        pil_image.show()

    else:
        print('multi face not support or empty face')

    # Show the picture
    # pil_image.show()

    # area = (400, 400, 800, 800)
    # cropped_img = pil_image.crop(area)
    # cropped_img.show()