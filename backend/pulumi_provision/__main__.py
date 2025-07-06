
import pulumi
import pulumi_aws as aws
import os

bucket_name = os.getenv("BUCKET_NAME", "default-pulumi-bucket")

bucket = aws.s3.Bucket(bucket_name,
    bucket=bucket_name,
    acl="private")

pulumi.export("bucket_name", bucket.id)
