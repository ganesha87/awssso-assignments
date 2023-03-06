import boto3

bucketName = 'tf-states-demo'
s3 = boto3.resource('s3')

s3.meta.client.download_file(bucketName, 'assignments/terraform.tfstate', './terraform/terraform.tfstate')
