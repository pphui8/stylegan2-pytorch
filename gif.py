from PIL import Image
import os

# Set the directory where the images are saved
image_dir = "asain_face/sample/"

# Set the name of the output GIF file
gif_name = "sample.gif"

# Set the duration (in milliseconds) for each frame of the GIF
frame_duration = 100

# Set the number of frames to skip between each included frame
skip_frames = 4

# Get the list of image file names
image_files = sorted(os.listdir(image_dir))

trim_range = 200

# Calculate the number of images to skip at the beginning and end of the sequence
num_skip_start = min(len(image_files) - 1, trim_range)
num_skip_end = min(len(image_files) - num_skip_start - 1, trim_range)

# Load the images and resize them to the same size
images = []
for i, image_file in enumerate(image_files[num_skip_start:len(image_files)-num_skip_end]):
    if i % skip_frames == 0:
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)
        image = image.resize((256, 256))
        images.append(image)

# Save the images as a GIF
images[0].save(
    gif_name,
    save_all=True,
    append_images=images[1:],
    duration=frame_duration,
    loop=0,
)