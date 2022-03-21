import boto3

s3 = boto3.resource('s3')

print('Name;Versioning;MFA_Delete;Rules')
for bucket in s3.buckets.all():
    b_name = bucket.name

    # BucketVersioning
    try:
        b_versioning = s3.BucketVersioning(b_name)
        print('Bucket: {} - Versioning Status: {} - MFA Delete: {}'.format(b_name, b_versioning.status,
                                                                           b_versioning.mfa_delete))
    except:
        b_versioning = []

    # BucketLifecycle
    try:
        b_lifecycle = s3.BucketLifecycle(b_name)
        b_rules = b_lifecycle.rules
        print('***** RULES *****')
        print('Expiration Days: {}'.format(b_rules[0]['Expiration']['Days']))
        print('Rule Name: {}'.format(b_rules[0]['ID']))
        print('Status: {}'.format(b_rules[0]['Status']))
        print('Transition Days: {}'.format(b_rules[0]['Transition']['Days']))
        print('Transition StorageClass: {}'.format(b_rules[0]['Transition']['StorageClass']))
        break
    except:
        b_lifecycle = []
