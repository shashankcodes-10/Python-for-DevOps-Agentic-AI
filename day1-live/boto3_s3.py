import boto3

# Create S3 client
s3 = boto3.client("s3")

# Create bucket
bucket_name = "boto3-first-bucket-10"

s3.create_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' created successfully!")

# Upload file
file_name = "/Users/shashank10/ai-powered/python for devops/Python-for-DevOps-Agentic-AI/day1-live/hello.txt"

s3.upload_file(file_name, bucket_name, "hello.txt")

print(f"Data successfully uploaded to '{bucket_name}'")

# List all buckets
response = s3.list_buckets()

print("\nAll Buckets:")
for bucket in response["Buckets"]:
    print(bucket["Name"])