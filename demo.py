import torch
from torchvision import transforms
from PIL import Image

im=Image.open('a.jpg')
w,h=im.size

print(f'w:{w} h:{h}')
p1=transforms.RandomCrop((h,w),padding=100)
p2=transforms.RandomHorizontalFlip()

im.show()
for _ in range(5):
    im2=p2(im)
    im2.show()