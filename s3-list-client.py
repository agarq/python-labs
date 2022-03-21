import boto3

s3 = boto3.client('s3')
listBuckets = s3.list_buckets()

for bucket in listBuckets['Buckets']:
    name = bucket["Name"]
    ver = ''
    mfa = ''
    rep_rules = ''
    source_region = ''
    dest_bucket = ''
    dest_region = ''
    storage_class = ''

    # 'jjhws-hw-prod-c4t-content'
    b_rep = s3.get_bucket_replication(Bucket='jjhws-hw-prod-data-lake')

    b_resp_metadata = b_rep['ResponseMetadata']
    b_replic_config = b_rep['ReplicationConfiguration']

    print(b_resp_metadata)
    print(b_replic_config)

    print('**********************')

    b_rep_rules = b_replic_config['Rules']

    print(b_rep_rules[0])
    print(b_rep_rules[0]['ID'])
    print(b_rep_rules[0]['Status'])
    b_dest = b_rep_rules[0]['Destination']
    print(b_dest['StorageClass'])
    print(b_dest['Bucket'])
    break

'''
    b_ver = s3.get_bucket_versioning(Bucket=name)
    try:
        ver = b_ver['Status']
    except:
        ver = 'Disabled'

    try:
        mfa = b_ver['MFADelete']
    except:
        mfa = 'Disabled'

    print('Name: {} - Versioning: {} - MFA: {}'.format(name, ver, mfa))
'''




