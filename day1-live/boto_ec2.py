# creating ec2 using boto3 

import boto3

ec2 = boto3.client("ec2")

response = ec2.run_instances(
    ImageId="ami-0b6d9d3d33ba97d99",
    InstanceType="t3.micro",
    KeyName="ec-2-keypair",
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "boto3-ec2"
                }
            ]
        }
    ]
)

print("Instance ID:", response["Instances"][0]["InstanceId"])