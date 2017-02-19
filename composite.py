from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys

path = "input/"
out = "output/"
dirs = os.listdir( path )

logo = Image.open('logo.png', 'r')

#offset = (lg_w, lg_h)
offset = (32, 32)
logo = logo.resize(offset,Image.ANTIALIAS)
lg_w, lg_h = logo.size

FONT = 'Vera.ttf'
TEXT = 'azmoonestan.ir'

filesToRemove = [f for f in os.listdir(out)]
for f in filesToRemove:
	os.remove(out+f)

def water_logo():
	for item in dirs:
		if os.path.isfile(path+item):
			img = Image.open(path+item)
			img = img.convert('RGB')
			w,h = img.size
			offset =(0, h-lg_h)
			pos = (lg_w+1, h-lg_h+12)
			img.paste(logo,offset)
			f, e = os.path.splitext(path+item)
			add_watermark(img, TEXT, out + item, pos)
			print('out -->> '+item)

			
def add_watermark(img, text, out_file, pos):
	font = ImageFont.truetype(FONT, 16)
	draw = ImageDraw.Draw(img)
	_r,_g,_b=avg_img_color(img,pos);
	draw.text(pos,text,(255-_r,255-_g,155-_b),font=font)
	img.save(out_file, 'JPEG')
	
def avg_img_color(img,_pos):
	width, height = (_pos[0]+12,_pos[1]+12)
	
	r_total = 0
	g_total = 0
	b_total = 0
	
	try:
		count = 0
		for x in range(_pos[0], width):
			for y in range(_pos[1], height):
				r, g, b = img.getpixel((x,y))
				r_total += r
				g_total += g
				b_total += b
				count += 1
	except Exception:
		print('An Error Has Occered!')
		return (100,100,0)
	
	return ((int)(r_total/count), (int)(g_total/count), (int)(b_total/count))
 
if __name__ == '__main__':
	water_logo()
