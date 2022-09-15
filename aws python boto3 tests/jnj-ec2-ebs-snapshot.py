import boto3
from fn_create_csv import create_csv

ec2client = boto3.client('ec2')
response = ec2client.describe_regions()


def is_none(s):
    if s is None:
        return ''
    return str(s)


# creating list
lst_h = ['Region',
         'Instance Id',
         'Volume Id',
         'Snapshot Id',
         'Start Time (UTC)',
         'Progress',
         'State',
         'Volume Size (GiB)',
         'Encrypted']

lst_r = []
hss = False

for r in response['Regions']:
    regionName = r['RegionName']
    ec2 = boto3.resource('ec2', r['RegionName'])

    for instance in ec2.instances.all():
        volumeId = ""
        snapshotId = ""
        startTimeUtc = ""
        progress = ""
        state = ""
        volumeSize = ""
        encrypted = ""

        instanceId = instance.id

        for vol in instance.volumes.all():
            volumeId = vol.id
            hss = False

            for ss in vol.snapshots.all():
                hss = True
                snapshotId = ss.snapshot_id
                startTimeUtc = ss.start_time.strftime("%Y-%m-%d %H:%M:%S")
                progress = ss.progress
                state = ss.state
                volumeSize = ss.volume_size
                encrypted = ss.encrypted

                lst_r.append([regionName,
                              instanceId,
                              volumeId,
                              is_none(snapshotId),
                              is_none(startTimeUtc),
                              is_none(progress),
                              is_none(state),
                              is_none(volumeSize),
                              is_none(encrypted)])

        if not hss:
            lst_r.append([regionName,
                          instanceId,
                          volumeId,
                          is_none(snapshotId),
                          is_none(startTimeUtc),
                          is_none(progress),
                          is_none(state),
                          is_none(volumeSize),
                          is_none(encrypted)])
        instanceId = ""

create_csv('EC2-Volume-Snapshots', lst_h, lst_r, ';')
