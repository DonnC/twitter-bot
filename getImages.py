# get images from the net

from bs4 import BeautifulSoup
import requests
import os

# Ownai_url = 'https://ownai.co.zw/index.php?page=ownai&action=search&sCategory=art-collectibles-rare-items'

# ask the user for type of images to download
query = str(input("Enter your image search query: "))
img_url = 'https://pexels.com/search/' + query

print("[*] Downloading web page for url >>> ", img_url)
page = requests.get(img_url)
soup = BeautifulSoup(page.text, 'html.parser')

image_tags = soup.findAll('img')

if not os.path.exists('Images'):
    os.makedirs('Images')

os.chdir('Images')
# get number of images to use for numbering our pics in the folder
num_images = len(os.listdir())


for image in image_tags:
    try:
        pic_url = image['src']
        print("[*] Now downloading >>> ", pic_url)
        source = requests.get(pic_url)

        if source.status_code == 200:
            with open("image-" + str(num_images) + ".jpg", "wb") as f:
                img = requests.get(pic_url).content
                f.write(img)
                num_images += 1

    except Exception as e:
        print("Error downloading image > ", e)




