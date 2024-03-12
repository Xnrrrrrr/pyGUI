import ctypes
import os

SPI_SETDESKWALLPAPER = 0x0014

def set_wallpaper(image_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_filename)

    # Check if the file exists
    if not os.path.isfile(image_path):
        print(f"Error: The specified image file '{image_path}' does not exist.")
        return

    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print(f"Wallpaper set to '{image_path}'.")

if __name__ == "__main__":
    # Specify the filename of the image within the directory
    image_filename = "rain.jpg"

    # Call the function to set the wallpaper
    set_wallpaper(image_filename)
