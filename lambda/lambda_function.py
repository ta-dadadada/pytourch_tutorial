import base64
import os
import boto3
import json
from io import BytesIO
from PIL import Image
import numpy as np
# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super().default(obj)


def lambda_handler(event, context):
    try:
        image = event['body']
    except KeyError:
        return {'body': 'Body does not contain image file'}
    image = base64.b64decode(image)
    image = Image.open(BytesIO(image), 'r')
    image = np.array(image)
    image = image.tolist()
    # Bodyについて、
    # この例はMNISTの白黒画像のため、1チャネルであることを表現するためにリストで囲っている
    # pytorchのエンドポイントはバッチ処理を前提としているので、もう一重リストで囲っている
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=json.dumps([[image]]))
    result = np.array(json.loads(response['Body'].read().decode()))[0]
    probs = np.exp(result) / np.sum(np.exp(result))
    predicted = probs.argmax()
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({
            'prediction_index': predicted,
            'probability': probs[predicted],
        }, cls=NumpyEncoder),
    }

