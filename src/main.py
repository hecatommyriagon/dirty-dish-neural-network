from PIL import Image
import glob
import os
import argparse

def process_images(directory, pattern):
    """
    Processes image files matching a given pattern in the specified directory.

    Args:
        directory (str): Path to the directory containing the images.

    """
    # Get all image file paths matching the pattern
    image_files = glob.glob(os.path.join(directory, pattern))

    print(f"Found {len(image_files)} image files matching pattern '{pattern}' in '{directory}'.")

    # Process each image file
    for image_file in image_files:
        try:
            # Open the image using Pillow
            with Image.open(image_file) as img:
                print(f"Processing {image_file}: size {img.size}, mode {img.mode}")
                # Example: Resize the image
                img_resized = img.resize((128, 128))
                # Optionally save the resized image
                # img_resized.save(f'processed/{os.path.basename(image_file)}')
        except Exception as e:
            print(f"Error processing {image_file}: {e}")


def main():

    # Open the image
    img = Image.open("path/to/image.jpg")

    # Display the image (optional)
    img.show()

def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Process image files matching a pattern.")
    parser.add_argument("directory", type=str, help="Directory containing the image files")
    parser.add_argument("pattern", type=str, help="Pattern to match image files (e.g., '*.png')")
    args = parser.parse_args()

    # Call the processing function
    process_images(args.directory, args.pattern)

# Execute only if the script is run directly
if __name__ == "__main__":
    main()
