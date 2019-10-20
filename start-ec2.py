import boto3
client = boto3.client('ec2')
client.start_instances(InstanceIds=['i-067b5cf1eb725df89'])