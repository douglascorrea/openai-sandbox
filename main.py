import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_messages(messages):
    user_input = input("\nUSER: ");
    if user_input == "exit":
        return
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_response = response["choices"][0]["message"]["content"]
    print("\nASSISTANT: {}".format(assistant_response))
    messages.append({"role": "assistant", "content": assistant_response})
    generate_messages(messages)

def main():
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    generate_messages(messages)

if __name__ == "__main__":
    main()
