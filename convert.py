from PIL import Image
import os

def convert_png_to_jpg(input_path, output_path):
    # Відкриваємо зображення
    with Image.open(input_path) as img:
        # Конвертуємо зображення в RGB (щоб прибрати альфа-канал)
        rgb_img = img.convert('RGB')
        # Зберігаємо зображення у форматі JPG
        rgb_img.save(output_path, format='JPEG')

if __name__ == "__main__":
    input_path = 'D:\Work\py_project\images\image.png'  # Шлях до вашого PNG-зображення
    output_path = 'D:\Work\py_project\images\image.jpg'  # Шлях до збереження JPG-зображення

    # Переконайтеся, що директорія для збереження існує
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    convert_png_to_jpg(input_path, output_path)
    print(f"Конвертація завершена! Зображення збережено за адресою {output_path}")
