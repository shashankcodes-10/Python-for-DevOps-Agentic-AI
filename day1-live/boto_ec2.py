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
# terminating instance

print("Instance ID:", response["Instances"][0]["InstanceId"])

ec2.terminate_instances(
    InstanceIds=["i-0bf7726cbe628feba"]
)


# Wait until terminated

waiter = ec2.get_waiter("instance_terminated")

waiter.wait(
    InstanceIds=["i-0bf7726cbe628feba"]
)

print("Instance terminated")