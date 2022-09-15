import boto3
import time
import sys

lambda_client = boto3.client('lambda')

function_arns = []
retrieve_function_arns = 0
functions = lambda_client.list_functions()

for fn in functions['Functions']:
    retrieve_function_arns += 1
    function_arns.append(str(fn['FunctionArn']))

print("You have {} functions.".format(retrieve_function_arns))
if retrieve_function_arns == 0:
    print("The script will now exit")
    sys.exit()

