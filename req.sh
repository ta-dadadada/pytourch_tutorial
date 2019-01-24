#!/bin/sh
curl https://hoibacna05.execute-api.ap-northeast-1.amazonaws.com/default/TadaTestLambda -X POST -F "file=@test.png;type=image/png" -H "Content-Type:image/png"
