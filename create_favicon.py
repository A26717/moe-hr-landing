from PIL import Image, ImageDraw, ImageFont
import os

# Create a 64x64 image
img = Image.new('RGB', (64, 64), color='#1B5E20')
draw = ImageDraw.Draw(img)

# Draw gold border
draw.rectangle([2, 2, 62, 62], outline='#D4AF37', width=3)

# Draw text (using default font)
try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

draw.text((8, 8), "MOE", fill='#D4AF37', font=font)
draw.text((14, 36), "HR", fill='white', font=font)

# Save as ICO
img.save('favicon.ico', format='ICO', sizes=[(64, 64)])
print("✅ favicon.ico created successfully!")