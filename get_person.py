import face_recognition
import os

base = "/people_images/"

def get_match(img2, base = "./people_images/"):
  unknown_encoding = face_recognition.face_encodings(img2)
  print(len(unknown_encoding))
  if(len(unknown_encoding) > 0):
    unknown_encoding = unknown_encoding[0]
    for img_path in os.listdir(base):
      # print(img_path)
      img1 = face_recognition.load_image_file(base + img_path)
      known_encoding = face_recognition.face_encodings(img1)

      if len(known_encoding) > 0:
        results = face_recognition.compare_faces(known_encoding, unknown_encoding)
        # print(results)
        
        if results[0]:
          return img_path
        



def main():
    img_path = "obama.jpg"
    img1 = face_recognition.load_image_file(img_path)

    matche = get_match(img1)

    print(matche)

if __name__ == '__main__':
    main()



