import os
from PIL import Image
import json
path = 'data/'
if not os.path.isdir('clip'):
  os.mkdir('clip')



def get_info():
  for root, dirs, files in os.walk(path):
      for file in files:
          (filename, extension) = os.path.splitext(file)
          if (extension == '.txt'):
              jpg_path=path + filename + '.txt'
              with open(jpg_path, 'r') as f:
                face_info = json.loads(f.read())
                left = face_info["stMobile106"][0]['face106']['rect']['left']
                top = face_info["stMobile106"][0]['face106']['rect']['top']
                right = face_info["stMobile106"][0]['face106']['rect']['right']
                bottom = face_info["stMobile106"][0]['face106']['rect']['bottom']
                info = {'jpg_name':filename,'left':left, 'top':top, 'right':right, 'bottom':bottom}
                get_photo(info)

def get_photo(info):
  jpg_path = path + info['jpg_name'] + '.jpg'
  img = Image.open(jpg_path)
  img = img.crop((info["left"], info["top"], info["right"], info["bottom"]))
  img.save('clip/' + info['jpg_name'] + '.jpg')


if __name__ == '__main__':
    info = get_info()

