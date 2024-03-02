
import boto3

access_key = "AKIA3RSDCY4Z6PFUVFOJ"
secret_access_key = "nCbuh0HivyWB7zV"

bedrock_client = boto3.client("bedrock-runtime", access_key, secret_access_key
, region_name = "us-west-2")

bedrock_client.invoke_mode()
