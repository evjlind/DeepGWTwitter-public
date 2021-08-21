import openai
import json

with open('credentials.json') as cred_file:
    creds = json.loads(cred_file.read())
openai.api_key = creds['open_ai'][0]['secret_key']
openai.File("file-k4Vie3WIc8Gzysd66chIwml4").delete()
print(openai.File.list())