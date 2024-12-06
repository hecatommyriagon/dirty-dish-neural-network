from PIL import Image
import os
import numpy as np
from tensorflow.keras.models import load_model


def classify(input_path, output_path, target_width=278, target_height=348, bg_color=255):
    # Open the image file (JPEG, PNG, etc.) and convert to grayscale
    im = Image.open(input_path).convert("L")

    # Get current size
    w, h = im.size

    # Compute scale factor to preserve aspect ratio and fit inside target dimensions
    scale = min(target_width / w, target_height / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # Resize the image using high-quality downsampling
    im = im.resize((new_w, new_h), Image.LANCZOS)

    # Create a new grayscale image for the background
    new_im = Image.new("L", (target_width, target_height), bg_color)

    # Compute the position to center the resized image within the new canvas
    left = (target_width - new_w) // 2
    top = (target_height - new_h) // 2

    # Paste the resized image onto the new image
    new_im.paste(im, (left, top))

    # Determine output format based on the file extension
    ext = os.path.splitext(output_path)[1].lower()
    if ext in [".jpg", ".jpeg"]:
        new_im.save(output_path, "JPEG", quality=95)
    elif ext == ".png":
        new_im.save(output_path, "PNG")
    else:
        # Default to JPEG if no recognized extension is given
        new_im.save(output_path, "JPEG", quality=95)

    restored_model = load_model('src/data/models/cnn_model.keras')

    # Add batch dimension so that input shape is now (1, height, width, channels)
    image_batch = np.expand_dims(new_im, axis=0)

    # Make a prediction
    prediction = restored_model.predict(image_batch)
    print(f"Model predicted {round(prediction[0][0])}")

    return round(prediction[0][0])
