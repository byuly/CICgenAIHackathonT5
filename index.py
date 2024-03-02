import boto3
import json

access_key = "AKIA3RSDCY4Z6PFUVFOJ"
secret_access_key = "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"

bedrock_runtime_client = boto3.client("bedrock-runtime", region_name="us-west-2", 
                                      aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

prompt = "Describe how to cook an egg"


body = {
    "prompt": prompt,
    "temperature": 0.5,
    "maxTokens": 200,
}

response = bedrock_runtime_client.invoke_model(
    modelId="amazon.titan-text-lite-v1", body=json.dumps(body)
)

response_body = json.loads(response["body"].read())
completion = response_body["completions"][0]["data"]["text"]

          


