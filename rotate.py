import cv2
import os
import tqdm

data = os.listdir('/home/guoshibo/mmrotate/tools/data/split_ms_dota/test/images')
data_list = []
for i in data:
    if i.find('0006', 0, 8) != -1:
        data_list.append(i)
for i in tqdm.tqdm(data_list):
    data_path = '/home/guoshibo/mmrotate/tools/data/split_ms_dota/test/images/' + i
    #print(data_path)
    image = cv2.imread(data_path)
    cv2.imwrite(f'/home/guoshibo/mmrotate/rotate_image/images/{i}', image)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    true_name = i.replace('.png', '')
    cv2.imwrite(f'/home/guoshibo/mmrotate/rotate_image/images/{true_name}1.png', image)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(f'/home/guoshibo/mmrotate/rotate_image/images/{true_name}2.png', image)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(f'/home/guoshibo/mmrotate/rotate_image/images/{true_name}3.png', image)