from PIL import Image
import pyperclip
image = Image.open(input("Paste the full file name here: "))
rgbimage = image.convert("RGB")
output = ""
print(image.size)
i = 1 
for y in range(image.size[1]):
    for x in range(image.size[0]):
        colorset = rgbimage.getpixel((x,y))
        colorset = [str(a) for a in colorset]
        for index, a in enumerate(colorset):
            if len(a) == 2:
                colorset[index] = "0"+ colorset[index]
            elif len(a) == 1:
                colorset[index] = "00"+ colorset[index]
        colorstr = str(colorset).replace(',', '').replace(' ', '').replace("[","").replace("]","").replace("'", "")
        output = output + colorstr
        i +=1
pyperclip.copy(output)  
spam = pyperclip.paste()  