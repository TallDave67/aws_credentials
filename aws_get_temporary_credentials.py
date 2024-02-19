import boto3
import sys

def get_temporary_credentials(access_key_id, secret_access_key):
    # Create an STS client
    sts_client = boto3.client('sts', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    # Assume a role to get temporary credentials
    response = sts_client.get_session_token()

    # Extract temporary credentials from the response
    credentials = response['Credentials']
    return credentials

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_s3_bucket.py <access_key_id> <secret_access_key>")
        sys.exit(1)

    access_key_id = sys.argv[1]
    secret_access_key = sys.argv[2]

    # Get temporary credentials
    temporary_credentials = get_temporary_credentials(access_key_id, secret_access_key)

    # Print the temporary credentials
    print("Temporary Credentials:")
    print("Access Key ID:", temporary_credentials['AccessKeyId'])
    print("Secret Access Key:", temporary_credentials['SecretAccessKey'])
    print("Session Token:", temporary_credentials['SessionToken'])
    print("Expiration:", temporary_credentials['Expiration'])