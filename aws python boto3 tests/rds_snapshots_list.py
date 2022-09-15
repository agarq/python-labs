
import boto3
client = boto3.client('rds')

response = client.describe_db_snapshots()

for i in response['DBSnapshots']:
    print(i['DBSnapshotIdentifier'])


#print(response)
