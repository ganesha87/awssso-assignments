import boto3

bucketName = 'tf-states-demo'
s3 = boto3.resource('s3')
#s3://tf-states-demo/assignments/terraform.tfstate
s3.meta.client.download_file(bucketName, 'assignments/terraform.tfstate', './config/assgn.tfstate')
s3.meta.client.download_file(bucketName, 'permissionsets/terraform.tfstate', './config/psets.tfstate')