# AWS SQS client Docker image

This image is serves a client for sending messages to [AWS SQS](https://aws.amazon.com/sqs/) queues.

The image uses [boto3](https://github.com/boto/boto3) AWS SDK.

The `aws-sqs-client` serves ATM only for sending single message to the AWS SQS queue. This might be changed in the future and more functionality may be added.

## Preparation

To be able to use this image, you will need AWS account and SQS queue.

### Create AWS secret and access key

To obtain AWS access and secret key, simply follow [the instructions](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).

### Create AWS SQS queue

To create AWS SQS queue - you can simply use the console. The complete guide explaining how to create simple SQS queue can be found in the [AWS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html).

### Send messages to AWS SQS queue

The Docker image uses a set of environment variables that a user needs to provide. Please fill out the following parameters 
in a new properties file.

_aws-sqs-client.properties_
```
AWS_ACCOUNT_ID=
AWS_SQS_QUEUE_NAME=
AWS_REGION=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SQS_TEXT=Hello
```            

```shell script
docker run -i --rm --env AWS_SQS_TEXT=Hello --env-file aws-sqs-client.properties tplevko/aws-sqs-client
```

Once you run this command, you should be able to see the message in the AWS SQS queue. You can verify this for instance in the [AWS SQS console](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html#step-receive-delete-message).

Please add the account information to the file `aws-sqs-credentials.properties` so the test can use it to connect to the Telegram API.
