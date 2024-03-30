import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import time
from siamese import Siamese

import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from siamese import Siamese
def calculate_similarity_threaded(directory, directory_path, files):
    model = Siamese()
    similarities = []
    for file in files:
        full_file_path = os.path.join(directory_path, file)
        try:
            comparison_image = Image.open(full_file_path)
            similarity = model.detect_image(image, comparison_image)
            similarities.append(similarity)
        except Exception as e:
            print(f"Error opening image {full_file_path}: {e}")
    average_similarity = sum(similarities) / len(similarities) if similarities else 0
    return directory, average_similarity  # 返回目录名称和相似度平均值

def calculate_similarity(image_path, directory_paths, stability):
    start_time = time.time()  # 开始时间
    image = Image.open(image_path)  # 提前打开图像，以便在多线程中使用
    with ThreadPoolExecutor() as executor:
        futures = []
        for directory, directory_path in directory_paths.items():
            files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))][:stability]
            futures.append(executor.submit(calculate_similarity_threaded, directory, directory_path, files))
        
        total_similarity = {}
        all_similarities = []
        for future in futures:
            directory, similarity = future.result()  # 解包返回的目录名称和相似度平均值
            total_similarity[directory] = similarity
            all_similarities.append(similarity)
        end_time = time.time()  # 结束时间
        print(f"calculate_similarity took {end_time - start_time} seconds")  # 打印用时
        return total_similarity, all_similarities


def calculate_probabilities(similarity_values):
    total_similarity = sum(similarity_values.values())
    probabilities = {key: value / total_similarity for key, value in similarity_values.items()}
    return probabilities

def plot_probabilities(probabilities):
    print("Probabilities dictionary:", probabilities)  # Debug print

    categories = list(probabilities.keys())
    values = list(probabilities.values())

    print("Categories:", categories)  # Debug print
    print("Values:", values)  # Debug print

    # Ensure all values are floats
    values = [float(value) for value in values]

    plt.bar(categories, values, color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Probability')
    plt.title('Category Probabilities')
    im = plt.gcf()
    im.savefig('results1.jpg')
    #plt.show()

if __name__ == "__main__":
    image_path = r"C:\Users\卢易航\Desktop\井盖隐患识别系统v1.0\Siamese\05-test.png"
    stability = 150#稳定度
    try:
        image = Image.open(image_path)
    except:
        print('Image Open Error! Try again!')
        exit(1)

    directories = {
        'good': 'datasets/images_background/good',
        'broke': 'datasets/images_background/broke',
        'uncovered': 'datasets/images_background/uncovered',
        'circle': 'datasets/images_background/circle',
        'lose': 'datasets/images_background/lose',
    }

    similarity_values, all_similarities = calculate_similarity(image_path, directories, stability)
    probabilities = calculate_probabilities(similarity_values)
    plot_probabilities(probabilities)

    max_category = max(probabilities, key=probabilities.get)
    print(f"The input image belongs to the category: {max_category}")
