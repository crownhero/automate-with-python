import docker

# Initialize the Docker client
client = docker.from_env()

# Define a list of image names or IDs that you want to exclude from deletion
excluded_images = ["c5a608b016a9 ", "98b8de62787c", "8df509127302", "20a3732f422b"]

# Get a list of all Docker images and containers
all_images = client.images.list()
all_containers = client.containers.list(all=True, filters={"status": "exited"})
# Iterate through the images and delete them if not in the exclusion list
for image in all_images:
    image_id = image.id
    image_tags = image.tags

    # Check if the image should be excluded from deletion
    should_exclude = any(tag in image_tags for tag in excluded_images)

    if not should_exclude:
        print(f"Deleting Docker image {image_id}...")
        client.images.remove(image=image_id, force=True)

print("All Docker images (except excluded ones) have been deleted.")

for containers in all_containers:
    containers_id = containers.id
    containers.remove(container=containers_id, force=True)

print("All conatiners removed successfully....")
