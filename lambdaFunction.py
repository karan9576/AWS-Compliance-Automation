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
    


#event = {
#   "version":"0",
#   "id":"5a06b07c-7d8b-1fb1-85c8-ca0a581397b9",
#   "detail-type":"EBS Volume Notification",
#   "source":"aws.ec2",
#   "account":"021891585312",
#   "time":"2024-08-11T11:11:51Z",
#   "region":"eu-north-1",
#   "resources":[
#       "arn:aws:ec2:eu-north-1:021891585312:volume/vol-0f0e09dd2ec13c47a"
#    ],
#    "detail":{
#       "result":"available",
#       "cause":"",
#       "event":"createVolume",
#       "request-id":"6ec0b4ea-d6c9-450f-950f-a51b746dbd80"
#    }
# }
