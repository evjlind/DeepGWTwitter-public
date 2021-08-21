import openai
import jsonlines
import json
import requests
import time

with open('credentials.json') as cred_file:
    creds = json.loads(cred_file.read())
openai.api_key = creds['open_ai'][0]['secret_key']
openai.File.create(
    file=open("fine_tune_data.jsonl", encoding='utf-8'),
    purpose='fine-tune'
)
time.sleep(120)
response = openai.File.list()
print(response)