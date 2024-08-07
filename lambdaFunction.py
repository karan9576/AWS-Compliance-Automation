import boto3

def extractVolumeID(volume_arn):
    arn_parts=volume_arn.split(':')
    vol_id= arn_parts[-1].split('/')[-1]
    return vol_id

def lambda_handler(event, context):
   
    volume_arn=event['resources'][0]
    volume_id=extractVolumeID(volume_arn)
    
    ec2_client=boto3.client('ec2')
    
    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
        Size=100 
    )   
    
    
