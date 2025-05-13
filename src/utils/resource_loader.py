"""
resource_loader.py - Resource loading utilities
"""

import os
import sys
import glob
from PyQt6.QtCore import QDir


def setup_resources():
    """Set up the application resources"""
    # Ensure base directories exist
    ensure_directories()

    # Add the root directory to the Python path if needed
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_dir not in sys.path:
        sys.path.append(root_dir)


def ensure_directories():
    """Ensure that all required directories exist"""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    dirs = [
        os.path.join(base_dir, "assets"),
        os.path.join(base_dir, "assets", "fonts"),
        os.path.join(base_dir, "assets", "images"),
        os.path.join(base_dir, "assets", "sounds"),
        os.path.join(base_dir, "assets", "music"),
    ]

    for directory in dirs:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            except Exception as e:
                print(f"Error creating directory {directory}: {e}")


def get_asset_path(asset_type, asset_name):
    """Get the full path to an asset

    Args:
        asset_type: Type of asset (fonts, images, sounds, music)
        asset_name: Name of the asset file

    Returns:
        Full path to the asset
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base_dir, "assets", asset_type, asset_name)


def find_assets(asset_type, pattern="*"):
    """Find assets matching a pattern

    Args:
        asset_type: Type of asset (fonts, images, sounds, music)
        pattern: Glob pattern to match

    Returns:
        List of matching asset paths
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    asset_dir = os.path.join(base_dir, "assets", asset_type)

    if not os.path.exists(asset_dir):
        return []

    return glob.glob(os.path.join(asset_dir, pattern))


def create_placeholder_assets():
    """Create placeholder assets for development"""
    # Create placeholder military font
    import urllib.request

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Font URLs - you can replace these with actual military-style fonts
    fonts = [
        {
            "url": "https://example.com/military_font.ttf",  # Replace with actual URL
            "path": os.path.join(base_dir, "assets", "fonts", "military_font.ttf")
        }
    ]

    for font in fonts:
        if not os.path.exists(font["path"]):
            try:
                urllib.request.urlretrieve(font["url"], font["path"])
                print(f"Downloaded font: {font['path']}")
            except Exception as e:
                print(f"Error downloading font {font['url']}: {e}")