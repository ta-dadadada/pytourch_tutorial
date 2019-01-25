# pytorch の練習

## API Gateway + Lambda で公開してみる

lambda function は次のような形で zip にする。
10MB を超える場合はS3経由でアップする必要があることに注意。
 

```
cd lambda
pip install numpy pillow -t .
zip -r ../lambda_function.zip .
```

* zip ファイルと python ファイルの basename は揃えたほうが良さそう？
* basename は変更可能だが、lambda での handler 設定を適切に変更しないと import error になる

API Gateway と Lambda の準備は、 Lambda 関数の作成から行うのが便利（辿って Gateway の構築に飛べるので）。

Gateway で COR を有効にするのを忘れない。

Sagemaker のエンドポイント名は、 Labmdaの環境変数として埋めることにしている。
設定忘れると当然動かない。

今のバージョンはバイナリサポートを有効にして作っている。
無効のまま構築できるかはわからない
（s3への画像アップロードにフックしてLambdaを起動したりはできるはずだが、
それでリアルタイム応答するAPIが作れるのかはわからない。たぶんできない）。


