import boto3

s3 = boto3.resource('s3')

print('Name;Versioning;MFA_Delete;Rules')
for bucket in s3.buckets.all():
    print(bucket.name)
