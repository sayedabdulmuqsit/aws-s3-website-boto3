import boto3

s3 = boto3.client('s3', region_name='eu-north-1')

bucket_name = 'muqsit-portfolio-site'

#s3.create_bucket(
 #   Bucket=bucket_name,
  #  CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'}
#)

#print(f"Bucket created: {bucket_name}")

s3.upload_file(
    'index.html',
    bucket_name,
    'index.html',
    ExtraArgs={'ContentType': 'text/html'}
)

print("index.html uploaded!")
# Public access block hatao
s3.delete_public_access_block(Bucket=bucket_name)

# Bucket policy set karo (public read)
import json
policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicRead",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": f"arn:aws:s3:::{bucket_name}/*"
    }]
}
s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(policy)
)

# Static website hosting enable karo
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'},
        'ErrorDocument': {'Key': 'error.html'}
    }
)

print(f"Website live: http://{bucket_name}.s3-website.eu-north-1.amazonaws.com")