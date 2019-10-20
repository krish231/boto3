import boto3
client = boto3.client('ec2')
resp = client.describe_instances(InstanceIds=['i-067b5cf1eb725df89'])
print(resp)

vpc_id = resp['Reservations'][0]['Instances'][0]['VpcId']
pub_ip = resp['Reservations'][0]['Instances'][0]['PublicIpAddress']

print(vpc_id)
print(pub_ip)



