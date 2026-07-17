import sys
from PIL import Image

def make_square(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    # Calculate the side length of the square
    size = max(width, height)
    
    # Create a new square image with a transparent background
    square_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    
    # Calculate the paste position to center the original image
    x = (size - width) // 2
    y = (size - height) // 2
    
    # Paste the original image into the square
    square_img.paste(img, (x, y))
    
    # Save the new square image
    square_img.save(out_path, format="PNG")
    print(f"Saved square image to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pad_image.py <input> <output>")
        sys.exit(1)
    make_square(sys.argv[1], sys.argv[2])
