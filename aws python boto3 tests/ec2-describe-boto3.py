import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances

client = boto3.client('ec2')

resp = client.describe_instances()

for res in resp['Reservations']:
    for instance in res['Instances']:
        print("Instance Id is {}".format(instance['InstanceId']))

