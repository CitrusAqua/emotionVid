import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PIL import Image, ImageOps, ImageFont, ImageDraw

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

happy       = 9
neutral     = 13
sad         = 1
surprise    = 3
angry       = 0
fear        = 0

emotion_list = ['Happy','Neutral','Sad','Surprise','Angry','Digest']
count_list = [9,13,1,3,0,0]

fig = plt.figure(figsize=(8, 3), dpi=80)
ax = fig.gca()

fig_w, fig_h = fig.get_size_inches() * fig.get_dpi()
fig_w = int(fig_w)
fig_h = int(fig_h)

xs = list(np.arange(-2.8, 0.2, 0.2))


barlist = ax.barh(range(6), count_list, tick_label=emotion_list)
barlist[0].set_color('y')
barlist[1].set_color('#00FFFF')
barlist[2].set_color('#0000FF')
barlist[3].set_color('#00FF00')
barlist[4].set_color('#FF0000')
barlist[5].set_color('#FF00FF')

'''
ax.plot(xs, happy, color='y', label='happy')
ax.plot(xs, neutral, color='#00FFFF', label='neutral')
ax.plot(xs, sad, color='#0000FF', label='sad')
ax.plot(xs, surprise, color='#00FF00', label='surprise')
ax.plot(xs, angry, color='#FF0000', label='angry')
ax.plot(xs, fear, color='#FF00FF', label='fear')
ax.grid()
ax.set_xlim([-2.8,1])
#ax.set_ylim([0,20])
'''

canvas = FigureCanvas(fig)
canvas.draw()
figure_img = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape(fig_h, fig_w, 3)
figure_img = Image.fromarray(figure_img)

extra = fig_h

img = Image.open('sample.png')
img_w, img_h = img.size
new_height = img_h + extra
bg = Image.new(img.mode, (img_w, new_height), (255, 255, 255))

bg.paste(img, (0, 0))
bg.paste(figure_img, (img_w - fig_w, img_h))


fnt40 = ImageFont.truetype("times.ttf", 40)
fnt32 = ImageFont.truetype("times.ttf", 32)
d = ImageDraw.Draw(bg)

d.text((70,img_h+fig_h*0.1), "Most common: ", font=fnt40, fill=(0,0,0))
d.text((70,img_h+fig_h*0.3), "2nd most common: ", font=fnt32, fill=(0,0,0))
d.text((70,img_h+fig_h*0.45), "3nd most common: ", font=fnt32, fill=(0,0,0))

d.text((360,img_h+fig_h*0.1), "neutral", font=fnt40, fill=(0,0,0))
d.text((360,img_h+fig_h*0.3), "happy", font=fnt32, fill=(0,0,0))
d.text((360,img_h+fig_h*0.45), "surp", font=fnt32, fill=(0,0,0))

bg.show()

#plt.show()