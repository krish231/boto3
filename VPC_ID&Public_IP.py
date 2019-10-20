import boto3
client = boto3.client('ec2')
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation["Instances"]:
        print(instance['VpcId'])

        if 'PublicIpAddress' in instance:
            public_ip= instance['PublicIpAddress']
            print (f'Public Ip address is {public_ip}')
        else:
            print('Public IP not found')
