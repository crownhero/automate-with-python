import boto3

# Specify your AWS region and S3 bucket name
bucket_name = 'your-s3-bucket-name'
prefix = 'space/accounts/'  # The folder path within your S3 bucket where result.html is located
file_name = 'result.html'

# Create an S3 client
s3 = boto3.client('s3', region_name='your-aws-region')

try:
    # Get the result.html template content from S3
    response = s3.get_object(Bucket=bucket_name, Key=prefix + file_name)

    # Read the content of the template
    template_content = response['Body'].read().decode('utf-8')

    # Output the content of the template
    print(template_content)
except Exception as e:
    # If there is an error retrieving the object
    print("Error getting email template:", e)
