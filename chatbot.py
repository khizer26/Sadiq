API_KEY= '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'
import openai
import os
os.environ['OPENAI_Key']=API_KEY
openai.api_key=os.environ['OPENAI_Key']

loop=True   
while loop:     #keeps running until 'exit' is typed
    prompt=input('Hello.\nType your question or type exit if done!!\n')
    if prompt=='exit':
        loop=False
    else:
        response=openai.Completion.create(engine='text-davinci-003',prompt=prompt,max_tokens=200)
        print(response['choices'][0]['text'])