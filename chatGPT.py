import openai

# Set the API key for openai
openai.api_key = "YOURTOKEN!!!"

# Set the model engine to use
model_engine = "text-davinci-002"

# Set the initial prompt for the chatbot
prompt = "Hello, I am ChatGPT. How can I help you? \n"

while True:
    # Get the user's input
    user_input = input(prompt)

    # Generate a response from the GPT-3 model
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        #max_tokens: This parameter specifies the maximum number of tokens 
        # (i.e., words and punctuation) that the GPT-3 model should generate in its response. 
        # In this case, the model is set to generate a maximum of 1024 tokens. 
        # This helps to ensure that the response is not too long or unmanageable.
        max_tokens=1024,
        #n: This parameter specifies the number of completions to generate. 
        # In the case of this code, n is set to 1, which means that the GPT-3 model will generate 
        # only one response.
        n=1,
        #temperature: This parameter controls the randomness or creativity of the generated response. 
        # A higher temperature will result in a more random, creative response, 
        # while a lower temperature will result in a response that is more predictable
        # and faithful to the input data.
        temperature=0.5,
    )

    # Print the user's input and the response from the GPT-3 model
    response = completions.choices[0].text
    print("You:", user_input)
    print("ChatGPT:", response)
