import os

import boto3

def get_queue_url(region_name, account_id, queue):
    return 'https://sqs.{region_name}.amazonaws.com/{account_id}/{queue}'.format(region_name=region_name, account_id=account_id, queue=queue)
        
# Send message to SQS queue
def send(aws_access_key_id, aws_secret_access_key, region_name, queue, account_id, aws_sqs_text):
    sqs = boto3.client('sqs', 
                      aws_access_key_id=aws_access_key_id, 
                      aws_secret_access_key=aws_secret_access_key, 
                      region_name=region_name
                      )
    response = sqs.send_message(
        QueueUrl=get_queue_url(region_name, account_id, queue),
        DelaySeconds=10,
        MessageBody=(aws_sqs_text)
    )
    print(response['MessageId'])

if __name__ == '__main__':
    account_id=os.environ["AWS_ACCOUNT_ID"]
    region_name=os.environ["AWS_REGION"]
    queue=os.environ["AWS_SQS_QUEUE_NAME"]
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"]
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
    aws_sqs_text = os.environ["AWS_SQS_TEXT"]

    send(aws_access_key_id, aws_secret_access_key, region_name, queue, account_id, aws_sqs_text)
