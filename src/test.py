import urllib.parse

# エンコードされたURL
encoded_url = "https://bestrun.blob.core.windows.net/bestrun-hoshi/%E7%8C%AB%E3%81%AF%E3%81%B4%E3%81%AF%E3%81%B4.mp4"

# デコードされたURLを取得
decoded_url = urllib.parse.unquote(encoded_url)

print(decoded_url)