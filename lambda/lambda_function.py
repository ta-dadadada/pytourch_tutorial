# import json
# import base64
import numpy as np
import PIL
#
#
# def lambda_handler(event, context):
#     img_base64 = event['body']
#     img_data = base64.b64decode(img_base64)
#     img_np = np.fromstring(img_data, np.uint8)
#     return {
#         'statusCode': 200,
#         'body': json.dumps({
#             'array': img_np.tolist(),
#             }, )
#     }
import os
import boto3
import json

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    image = event['body']
    print(image, type(image))
    payload = image
    print(payload)

    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=payload)
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)
    return response
