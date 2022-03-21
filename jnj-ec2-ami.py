import boto3
import dateutil.parser
from fn_create_csv import create_csv

ec2client = boto3.client('ec2')

response = ec2client.describe_regions()

# creating list
lst_h = ['Region Id', 'Instance Id', 'Instance Name', 'Instance Type', 'Instance Status', 'AMI Id', 'AMI Name', 'AMI Creation Date']
lst_r = []

for r in response['Regions']:
    print('Region: {}'.format(r['RegionName']))
    ec2 = boto3.resource('ec2', r['RegionName'])

    for instance in ec2.instances.all():
        name = ""
        ami_name = ""
        ami_creation_date = ""

        image = instance.image

        for tag in instance.tags:
            if tag['Key'] == 'Name':
                name += tag['Value']

        try:
            ami_name = image.name
            ami_creation_date = dateutil.parser.parse(image.creation_date).strftime("%Y-%m-%d %H:%M:%S")

        except:
            ami_name = 'deleted or made private'
            ami_creation_date = ''

        lst_r.append([r['RegionName'],
                      instance.instance_id,
                      name,
                      instance.instance_type,
                      instance.state['Name'],
                      instance.image_id,
                      ami_name,
                      ami_creation_date])

create_csv('EC2-with-AMI', lst_h, lst_r, ';')
