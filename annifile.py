import os
import tqdm
data = os.listdir('/home/guoshibo/mmrotate/rotate_image/images')
for i in tqdm.tqdm(data):
    path = '/home/guoshibo/mmrotate/rotate_image/annfiles/' + i.replace('.png', '')
    with open(f'{path}.txt', 'w'):
        pass
# for i in tqdm.tqdm(data):
#     path = '/home/guoshibo/mmrotate/rotate_image/images/' + i
#     true_name = i.replace('.png', '.txt')
#     os.rename(path, f'/home/guoshibo/mmrotate/rotate_image//{true_name}')