import os
from PIL import Image

while True:
    x = 0
    y = 0
    width = 0
    height = 0

    ebook_name = input("Enter ebook name >> ")
    save_folder = os.path.join("ebooks", ebook_name)
    cropped_save_folder = os.path.join("ebooks", ebook_name + "_cropped")

    if not os.path.exists(save_folder):
        exit("No ebook found " + save_folder)

    if not os.path.exists(cropped_save_folder):
        os.makedirs(cropped_save_folder)

    num_pages = int(input("Enter the number of pages to be cropped >> "))
    # Crop pages
    for page in range(1, num_pages + 1):
        page_path = os.path.join(save_folder, f"page_{page}.png")
        cropped_page_path = os.path.join(cropped_save_folder, f"page_{page}.png")

        crop_box = (x, y, width, height)
        page_img = Image.open(page_path)
        cropped_page_img = page_img.crop(crop_box)
        cropped_page_img.save(cropped_page_path)

    if input("Press enter to crop next ebook or 0 to quit") == 0:
        exit()
