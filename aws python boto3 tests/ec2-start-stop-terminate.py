import boto3
# EC2 instanceID: i-0649754bcaa65ba22

client = boto3.client('ec2')

# start
# client.start_instances(InstanceIds=['i-0649754bcaa65ba22'])

# stop
# client.stop_instances(InstanceIds=['i-0fd05e030566305b6'])

# terminate
resp = client.terminate_instances(InstanceIds=['i-07d53b30796bef85a'])

for instance in resp['TerminatingInstances']:
    print('The instance with Id {} was terminated'.format(instance['InstanceId']))


