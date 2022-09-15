import boto3
from fn_create_csv import create_csv

client = boto3.client('iam', verify=False)
iam = boto3.resource('iam', verify=False)

roles = client.list_roles()
Role_list = roles['Roles']

def is_none(s):
    if s is None:
        return ''
    return str(s)

# creating list
lst_h = ['Account Name',
         'Account ID',
         'IAM Role Name',
         'Role Creation Date',
         'Role Last Activity',
         'Role ARN']

lst_r = []
hss = False

accountName = client.list_account_aliases()['AccountAliases'][0]
accountId = boto3.client('sts', verify=False).get_caller_identity().get('Account')

for key in Role_list:
    iamRoleName = key['RoleName']

    role = iam.Role(iamRoleName)
    
    roleCreationDate = role.create_date
    
    try:
        roleLastActivity = role.role_last_used["LastUsedDate"]
    except:
        roleLastActivity = "Not Specified"
    
    roleArn = role.arn

    lst_r.append([accountName,
                  is_none(accountId),
                  is_none(iamRoleName),
                  is_none(roleCreationDate),
                  is_none(roleLastActivity),
                  is_none(roleArn)])

#create report in csv format
create_csv('RnD-IAM-Roles', lst_h, lst_r, ';')
