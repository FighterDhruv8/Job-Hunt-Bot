def code(message):
    
    from openai import OpenAI
    
    with open('.\\API Keys\\Krutrim.txt', 'r') as f:
        key = f.read().strip()
    
    openai = OpenAI(
        api_key=key,
        base_url="https://cloud.olakrutrim.com/v1",
    )
    chat_completion = openai.chat.completions.create(
        model="Krutrim-spectre-v2",
        messages=[
            {"role": "system", "content": "You are a job hunting assistant."
                                           "Your task is to provide relevant jobs based on the provided skills (skills are given in no particular order)."
                                           "Format the output exactly like this: The possible jobs are : A list of the possible jobs, with a ^ symbol at the beginning of each job."},
            {"role": "user", "content": message}
        ],
        frequency_penalty= 0, # Optional, Defaults to 0. Range: -2 to 2
        logit_bias= {2435: -100, 640: -100},
        logprobs= True, # Optional, Defaults to false
        top_logprobs= 2, # Optional. Range: 0 to 50
        max_tokens= 256, # Optional
        n= 1, # Optional, Defaults to 1
        presence_penalty= 0, # Optional, Defaults to 0. Range: -2 to 2
        response_format= { "type": "text" }, # Optional, Defaults to text
        stop= None, # Optional, Defaults to null. Can take up to 4 sequences where the API will stop generating further tokens.
        stream= False, # Optional, Defaults to false
        temperature= 0, # Optional, Defaults to 1. Range: 0 to 2
        top_p= 1 # Optional, Defaults to 1. We generally recommend altering this or temperature but not both.
    )
    return chat_completion.choices[0].message.content