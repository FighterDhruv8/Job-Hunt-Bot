def code(message):
    import google.generativeai as genai

    with open(r'.\\API Keys\\Gemini.txt', 'r') as f:
            key = f.read().strip()
    
    genai.configure(api_key=key)
    model=genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction='''You are a job hunting assistant.
        Your task is to provide relevant jobs based strictly on the provided skills (skills are given in no particular order).
        Format the output exactly like this: The possible jobs are : A list of the possible jobs, with a ^ symbol at the beginning of each job.
        ''')
    response = model.generate_content(message)
    return response.text

print(code('Java, Python'))