import boto3
import dateutil.parser

ec2 = boto3.resource('ec2')
# i-0c5d5d9d58a6a2938
# i-06a64f5034e336f93 - SIN AMI
for instance in ec2.instances.filter(Filters=[
   {
       'Name': 'instance-id',
       'Values': ['i-06a64f5034e336f93']
   }
]):
    image = instance.image

    try:
        ami_name = image.name
        ami_creationdate = dateutil.parser.parse(image.creation_date).strftime("%Y-%m-%d %H:%M:%S")

    except:
        ami_name = 'deleted or made private'
        ami_creationdate = ''

    #fecha = dateutil.parser.parse(ami_creationdate)

    print('Instance ID: {} \nAMI Name: {} \nAMI ID: {} \nAMI CreationDate: {}'.format(instance.id, ami_name, instance.image_id, ami_creationdate))
