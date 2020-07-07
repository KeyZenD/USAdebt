from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests

api = requests.get("https://www.pgpf.org/pgpf-debt-stats/json/next-debt-slice")
debt = api.json()["gross_debt"]
gosdolg = f"{debt}"

img = Image.open("template.jpg")

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial_bold_italic.ttf", 60)
draw.text((240, 248), gosdolg, (255, 82, 82), font=font)

img.save('gosdolg.jpg')
