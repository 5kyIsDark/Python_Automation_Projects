from PIL import Image
import os 

image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
new_width = 800
target = input("please Enter The File Path with the images You want to resize: ").strip()
output = "Resized_Images"
os.makedirs(output, exist_ok=True)

for file in os.listdir(target):
    path = os.path.join(target, file)
    

    if os.path.isdir(path):
        continue

    name, ext = os.path.splitext(file)
    if ext.lower() not in image_extensions:
        continue

    try:
        img = Image.open(path)
        original_width, original_height = img.size
        new_height = int((new_width / original_width) * original_height)
        resized_img = img.resize((new_width, new_height))
        
        new_path = os.path.join(output, file)
        resized_img.save(new_path)
        print(f"✅ Resized and saved: {file}")
    except Exception as e:
        print(f"❌ Failed to process {file}: {e}")

tag = bytes.fromhex('536b7949734461726b').decode()