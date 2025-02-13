from PIL import Image, ImageDraw
import os

def create_gradient_background(width, height, start_color, end_color, filename):
    # Create new image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Generate gradient
    for y in range(height):
        r = start_color[0] + (end_color[0] - start_color[0]) * y / height
        g = start_color[1] + (end_color[1] - start_color[1]) * y / height
        b = start_color[2] + (end_color[2] - start_color[2]) * y / height
        draw.line([(0, y), (width, y)], fill=(int(r), int(g), int(b)))
    
    # Save the image
    image.save(filename)

# Create Images_GUI directory if it doesn't exist
if not os.path.exists("Images_GUI"):
    os.makedirs("Images_GUI")

# Create login background (dark blue gradient)
create_gradient_background(1366, 768, (26, 26, 26), (13, 13, 13), "Images_GUI/login_bg.png")

# Create dashboard background (dark theme)
create_gradient_background(1366, 768, (26, 26, 26), (13, 13, 13), "Images_GUI/dashboard_bg.png")

print("Background images created successfully!") 