import requests

url = 'https://exp.cdn-hotels.com/hotels/34000000/33460000/33457100/33457035/1ae8596b_w.jpg'
name = input('как сохранить?')

img = requests.get(url)
with open(name + '.jpg', 'wb') as file:
    file.write(img.content)
# img_option = open(name + '.jpg', 'wb')
# img_option.write(img.content)
# img_option.close()n