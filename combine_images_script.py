from PIL import Image
import os

# Paths to the directories
v1_dir = 'predictions_plots_v1/'
v2_dir = 'predictions_plots_v2/'
output_dir = 'combined_plots_1_vs_2/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Get a list of image files from both directories
v1_images = sorted(os.listdir(v1_dir))
v2_images = sorted(os.listdir(v2_dir))

# Iterate through images in both directories
for v1_image, v2_image in zip(v1_images, v2_images):
    # Open the images
    img1 = Image.open(os.path.join(v1_dir, v1_image))
    img2 = Image.open(os.path.join(v2_dir, v2_image))

    # Get dimensions
    width1, height1 = img1.size
    width2, height2 = img2.size

    # Create a new image that will hold both images side by side
    combined_image = Image.new('RGB', (width1 + width2, max(height1, height2)))

    # Paste images into the new image
    combined_image.paste(img1, (0, 0))
    combined_image.paste(img2, (width1, 0))

    # Save the result
    combined_image.save(os.path.join(output_dir, f'combined_{v1_image}'))

print("Images combined and saved successfully.")