import boto3
from fn_create_csv import create_csv

iam = boto3.resource('iam', verify=False)
role = iam.Role('<role-name>')

print(role.arn)
print(role.create_date)
print(role.role_last_used["LastUsedDate"])