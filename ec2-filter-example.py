import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(Filters=[
   {
       'Name': 'instance-id',
       'Values': ['i-0b2b85f70b4ecff8b']
   }
]):
    for vol in instance.volumes.all():
        print(vol.snapshots.all())
        '''
        iid = vol.attachments[0]['InstanceId']
        state = vol.attachments[0]['State']
        sid = vol.snapshot_id.strip()
        v = vol.id

        if len(sid) == 0:
            print('{};;;;;;;;'.format(iid))
        else:
            print(iid, v, state, sid)
'''


