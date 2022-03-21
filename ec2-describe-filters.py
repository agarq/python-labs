import boto3
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
client = boto3.client('ec2')

'''
# filtramos por el estado (en ejecución, detenida)
resp = client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running', 'stopped']
}])
'''
# filtramos por Tag Environment = prod
resp = client.describe_instances(Filters=[{
    'Name': 'tag:Environment',
    'Values': ['prod']
}])

for res in resp['Reservations']:
    for instance in res['Instances']:
        print("Instance Id is {}".format(instance['InstanceId']))

