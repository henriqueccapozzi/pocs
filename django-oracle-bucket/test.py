import boto3
  
s3 = boto3.resource(
    's3',
    aws_access_key_id="e06cf98c82f650a11fa57246cd907f9703321fca",
    aws_secret_access_key="40GXj2OXXqASrEQZ+5jzlzO1zlNu4jUKcS0QL41R2+E=",
    region_name="sa-saopaulo-1", # Region name here that matches the endpoint
    endpoint_url="https://grcqunjr5vfy.compat.objectstorage.sa-saopaulo-1.oraclecloud.com" # Include your namespace in the URL
)
# https://objectstorage.sa-saopaulo-1.oraclecloud.com
  
# Print out the bucket names
for bucket in s3.buckets.all():
    print (bucket.name)