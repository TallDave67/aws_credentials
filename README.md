# Credentials

Scripts to get temporary credentials and to get the caller identity given permanent/temporary credentials.

## Get Temporary Credentials

Parameters:

Permanent Access Key Id

Permanent Secret Access Key

Note that an AWS Permanent Access Key starts with AKIA, but the temporary one starts with ASIA.

## Get Caller Identity

Parameters:

Permanent/Temporary Access Key Id

Permanent/Temporary Secret Access Key

(OPTIONAL) Session Token

The Session Token must be passed if you are using temporary credentials

## Tests

### Get Temporary Credentials

![Shell](tests\tests01_get_temporary_credentials.png)

### Create S3 Bucket with Temporary Credentials

![Shell](tests\tests02_create_s3_bucket_with_temporary_credentials.png)

![AWS Console](tests\tests03_see_s3_bucket.png)

