from PIL import Image
import os

def convert_png_to_jpg(input_path, output_path):
    with Image.open(input_path) as img:
        rgb_img = img.convert('RGB')
        rgb_img.save(output_path, format='JPEG')

if __name__ == "__main__":
    input_path = 'D:\Work\py_project\images\image.png'  
    output_path = 'D:\Work\py_project\images\image.jpg' 

os.makedirs(os.path.dirname(output_path), exist_ok=True)

convert_png_to_jpg(input_path, output_path)
print(f"Конвертація завершена! Зображення збережено за адресою {output_path}")
