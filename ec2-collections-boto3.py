import boto3
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html
ec2 = boto3.resource('ec2')
'''
# ejemplo 1: consultar todas las instancias
for instance in ec2.instances.all():
# se pueden consultar los atributos de instance aqui: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
    print('Instance ID is {} and Type is {}'.format(instance.instance_id, instance.instance_type))

# ejemplo 2: filtrar las instancias por zona de disponibilidad
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1d']
    }
]):
    print('Instance ID is {} and Type is {}'.format(instance.instance_id, instance.instance_type))
'''
# ejemplo 3: detener todas las instancias en ejecución
ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]).stop()

