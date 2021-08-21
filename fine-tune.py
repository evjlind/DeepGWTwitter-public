import openai
import json
import time

with open('credentials.json') as cred_file:
    creds = json.loads(cred_file.read())
openai.api_key = creds['open_ai'][0]['secret_key']
#openai.FineTune.create(training_file="file-PMapXKc9HCqleQLZhXORhT6l")

#openai.FineTune.cancel(id="ft-aBBudKmhAXyZBadH6C0em2IP")
#response = openai.FineTune.list()
response = openai.FineTune.retrieve(id="ft-10diMAAuKcQ7ZJo4tw5LGq2n")
print(response)