import boto3
import json


access_key = "AKIA3RSDCY4Z6PFUVFOJ"
secret_access_key = "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"

bedrock_runtime_client = boto3.client("bedrock-runtime", region_name="us-west-2", 
                                      aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)


inputs = []

while True:
    user_input = input("Please enter a symptom (or type 'n/a' to stop): ")
    if user_input.lower() == "n/a":
        break
    inputs.append(user_input)

prompt = "I feel sick, my symptoms are: "
prompt += ", ".join(inputs) + "."
prompt += "What do you think these symptoms point to?"
prompt += "Only list the illnesses, no other words. just give me the words of the illnesses, like 'cold' or like 'cold, flu'"
prompt += " and just must give me the ONLY list of the illness using array, for example, [infection, flu, cold]"
print(prompt)


body = {
    "prompt": prompt,
    "temperature": 0.5,
    "maxTokens": 200,
}

response = bedrock_runtime_client.invoke_model(
    modelId="ai21.j2-ultra-v1", body=json.dumps(body)
)

response_body = json.loads(response["body"].read())
completion = response_body["completions"][0]["data"]["text"]

def extract_illnesses(input_string):
    # Find the index of '[' and ']'
    start_index = input_string.find('[')
    end_index = input_string.find(']')

    # Extract the substring containing the list
    list_string = input_string[start_index:end_index + 1]

    # Convert the string representation of the list to a Python list
    return eval(list_string)

# Extract the illnesses from the input string
illness_list = extract_illnesses(completion)
description_list = []
for i in illness_list:
    prompt = "Give me the description of the illness: " + i
    body = {
    "prompt": prompt,
    "temperature": 0.5,
    "maxTokens": 200,
    }

    response = bedrock_runtime_client.invoke_model(
        modelId="ai21.j2-ultra-v1", body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    completion = response_body["completions"][0]["data"]["text"]

    description_list.append(completion)

paragraph = "List of possible ilnesses: "
for i in range(len(illness_list)):
    paragraph += "\n\n"
    paragraph += illness_list[i] + ": " + description_list[i]

class Paragraph:
    def getParagraph():
        return paragraph


    




          


