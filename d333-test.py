# -*- coding: utf-8 -*-

import requests
import base64


# 获取文件的 Base64 编码结果
def get_content(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        data_b64 = base64.b64encode(data).decode('utf-8')  # 将二进制文件编码后转换为字符串形式
        return data_b64


def upload_file(content, file_name, repo_name, token):
    url = f"https://api.github.com/repos/GitHubYid/api-demo/contents/{file_name}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    data = {
        "message": "upload file",
        "committer": {
            "name": "username",
            "email": "xx@xx.com"
        },
        "content": content
    }
    import json
    req = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(req)


if __name__ == '__main__':
    token = "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" # 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
    data = get_content("demo.py")
    upload_file(data, "d333-test.py", "GitHubYid/api-demo", token)
