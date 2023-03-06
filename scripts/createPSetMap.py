import boto3

client = boto3.client('sso-admin')
instances = client.list_instances()
instanceARN = instances['Instances'][0]['InstanceArn']

permissionSets = client.list_permission_sets(InstanceArn=instanceARN,MaxResults=99)
print('permissionARN ={')
for pset in permissionSets['PermissionSets']:
        psetDetails = client.describe_permission_set(InstanceArn=instanceARN, PermissionSetArn=pset)
        print('  '+psetDetails['PermissionSet']['Name'] +'  =  "' +pset+'"')
print('}')
