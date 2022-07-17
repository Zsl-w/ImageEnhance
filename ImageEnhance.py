import base64
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from aip import AipImageProcess

""" 打开选择文件夹对话框 """
root = tk.Tk()
root.withdraw()


APP_ID = "Your APP_ID" 
APT_KEY = "Your APT_KEY"
SECRET_KEY = "Your SECRET_KEY"


client = AipImageProcess(APP_ID, APT_KEY, SECRET_KEY)


# folderPath = filedialog.askdirectory()  # 获得选择好的文件夹
img_path = filedialog.askopenfilename()  # 获得选择好的文件

"""读取图像"""


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" base64图片解码 """


def base64_to_image(base64_code):
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.frombuffer(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    return img


# img_path = r'2.jpeg'
# ori_img = cv2.imread(img_path)
image = get_file_content(img_path)

""" 调用图像清晰度增强 """
img = client.imageDefinitionEnhance(image)


img = img['image']
show_img = base64_to_image(img)

cv2.imwrite('%s.png' % (img_path.split('.')[
            0]+'-enhance'), show_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
