import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    instance_id = "i-00e339b27190269b0"   # your EC2 instance

    response = ec2.start_instances(InstanceIds=[instance_id])
    print(response)

    return {"message": "EC2 started"}
