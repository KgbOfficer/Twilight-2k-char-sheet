"""
image_setup.py - Create necessary placeholder images
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys


def create_placeholder_image(path, width, height, text=None, bg_color=(80, 80, 80), text_color=(200, 200, 200)):
    """Create a placeholder image with optional text

    Args:
        path: Path to save the image
        width: Image width
        height: Image height
        text: Optional text to display
        bg_color: Background color (RGB tuple)
        text_color: Text color (RGB tuple)
    """
    # Create the image with background color
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Add text if provided
    if text:
        try:
            # Try to use a system font
            font_size = min(width, height) // 10
            if sys.platform.startswith('win'):
                font = ImageFont.truetype("arial.ttf", font_size)
            else:
                # Use default font if specific font not available
                font = ImageFont.load_default()

            # Calculate text position to center it
            text_width, text_height = draw.textsize(text, font=font)
            position = ((width - text_width) // 2, (height - text_height) // 2)

            # Draw the text
            draw.text(position, text, fill=text_color, font=font)
        except Exception as e:
            print(f"Error adding text to image: {e}")
            # If text drawing fails, create a simple placeholder
            draw.rectangle([(width // 4, height // 4), (width * 3 // 4, height * 3 // 4)], outline=text_color)

    # Save the image
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    print(f"Created placeholder image at {path}")


def ensure_images():
    """Create necessary placeholder images"""
    # Background images
    backgrounds = [
        ("default_bg.png", 1024, 768, "Default Background"),
        ("military_bg.png", 1024, 768, "Military Background"),
        ("soviet_bg.png", 1024, 768, "Soviet Background")
    ]

    for filename, width, height, text in backgrounds:
        path = Path("assets/images/backgrounds") / filename
        if not path.exists():
            create_placeholder_image(path, width, height, text,
                                     bg_color=(40, 40, 40),
                                     text_color=(150, 150, 150))

    # Icons
    icons = [
        ("app_icon.png", 64, 64, "App"),
        ("dice.png", 32, 32, "Dice"),
        ("save.png", 32, 32, "Save"),
        ("export.png", 32, 32, "Export"),
        ("new.png", 32, 32, "New")
    ]

    for filename, width, height, text in icons:
        path = Path("assets/images/icons") / filename
        if not path.exists():
            create_placeholder_image(path, width, height, text,
                                     bg_color=(60, 60, 120),
                                     text_color=(220, 220, 220))

    print("All necessary placeholder images have been created.")


if __name__ == "__main__":
    try:
        ensure_images()
    except ImportError:
        print("Error: PIL not installed. Cannot create images.")
        print("Run 'pip install pillow' to install the required library.")

        # Create empty placeholder files instead
        print("Creating empty placeholder files instead...")

        # Background images
        backgrounds = [
            "default_bg.png",
            "military_bg.png",
            "soviet_bg.png"
        ]

        for filename in backgrounds:
            path = Path("assets/images/backgrounds") / filename
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "wb") as f:
                    # Write minimal PNG header
                    f.write(
                        b"\x89PNG\r\n\x1a\n\x00\x00\x00\x0dIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0aIDAT\x08\x99c\x00\x00\x00\x02\x00\x01\xe2\x21\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82")
                print(f"Created empty placeholder image at {path}")

        # Icons
        icons = [
            "app_icon.png",
            "dice.png",
            "save.png",
            "export.png",
            "new.png"
        ]

        for filename in icons:
            path = Path("assets/images/icons") / filename
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "wb") as f:
                    # Write minimal PNG header
                    f.write(
                        b"\x89PNG\r\n\x1a\n\x00\x00\x00\x0dIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0aIDAT\x08\x99c\x00\x00\x00\x02\x00\x01\xe2\x21\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82")
                print(f"Created empty placeholder image at {path}")