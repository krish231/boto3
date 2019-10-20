import boto3
client = boto3.client('ec2')
resp = client.describe_instances(
    Filters =[
    {
        'Name':'instance-state-name',
        'Values':['running']
    }
]
)
instance_ids = list()
for reservation in resp['Reservations']:
    for instance in reservation["Instances"]:
        instance_id= instance['InstanceId']
        instance_ids.append(instance_id)
        print(f'Instance id is {instance_id}')

client.stop_instances(
    InstanceIds=instance_ids
)