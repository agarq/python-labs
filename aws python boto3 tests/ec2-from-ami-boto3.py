import boto3
client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-00ddb0e5626798373',
                            InstanceType='t2.micro',
                            MinCount=1,
                            MaxCount=1,
                            KeyName='kp-ubuntu-test')
for instance in resp['Instances']:
    print(instance['InstanceId'])

