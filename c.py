from PIL import Image
import os

def flip_images_in_directory(input_directory, output_directory):
    # 确保输出目录存在
    os.makedirs(output_directory, exist_ok=True)
    
    # 遍历输入目录中的所有文件
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_directory)
                output_path = os.path.join(output_directory, relative_path)
                
                # 确保输出文件的目录存在
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 打开图像
                img = Image.open(input_path)
                
                # 左右翻转图像
                flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                
                # 保存翻转后的图像
                flipped_img.save(output_path)
                
                print(f"Flipped image saved at: {output_path}")

# 指定输入和输出目录
input_directory_train = 'dog&cat/archive/test_set/test_set'
output_directory_train = 'dog&cat/archive/test_set_reverse/test_set_reverse'

input_directory_test = 'archive/training_set/training_set'
output_directory_test = 'dog&cat/archive/train_set_reverse/train_set_reverse'

# 左右翻转并保存图像
flip_images_in_directory(input_directory_train, output_directory_train)
flip_images_in_directory(input_directory_test, output_directory_test)
