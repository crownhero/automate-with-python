import docker

# Initialize the Docker client
client = docker.from_env()

# Define a list of image names or IDs that you want to exclude from deletion
excluded_images = ["258da150107a","20a3732f422b"]

# Get a list of all Docker images
all_images = client.images.list()

# Iterate through the images and delete them if not in the exclusion list
for image in all_images:
    image_id = image.id
    image_tags = image.tags

    # Check if the image should be excluded from deletion
    should_exclude = any(tag in image_tags for tag in excluded_images)

    if not should_exclude:
        print(f"Deleting Docker image {image_id}...")
        client.images.remove(image=image_id, force=True)
