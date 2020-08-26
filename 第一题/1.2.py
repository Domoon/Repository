import os
from PIL import Image, ImageDraw
import json
path = 'data/'
if not os.path.isdir('data_106'):
  os.mkdir('data_106')



def get_info():
  for root, dirs, files in os.walk(path):
      for file in files:
          (filename, extension) = os.path.splitext(file)
          if (extension == '.txt'):
              jpg_path=path + filename + '.txt'
              with open(jpg_path, 'r') as f:
                face_info = json.loads(f.read())
                info = face_info["stMobile106"][0]['face106']['pointsArray']
                draw_point([info,filename])

def draw_point(info):
    jpg_path = path + info[-1] + '.jpg'
    img = Image.open(jpg_path)
    a =ImageDraw.Draw(img)
    for proxy in info[0]:
        a.point((proxy['x'], proxy['y']), fill=(0,0,255))

    img.save('data_106/' + info[-1] + '.jpg')



if __name__ == '__main__':
    info = get_info()



