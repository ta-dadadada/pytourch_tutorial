#!/bin/sh
path="<api gateway url>"  # ex) https://hogepiyo.execute-api.ap-northeast-1.amazonaws.com/default
api="<api name>"  # ex) /testLambda
curl -X POST --data-binary "@test.png" -H "Content-Type:image/png" "${path}${api}"
