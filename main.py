import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main(user_prompt, verbose = False):
    print("Hello from py-ai-agent!")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    contents = messages

    generate_content_response = client.models.generate_content(model = model, contents = contents)

    print(generate_content_response.text)
    if (verbose):
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {generate_content_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generate_content_response.usage_metadata.candidates_token_count}")

    return 0

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Prompt argument missing")
        sys.exit(1)
    if len(sys.argv) > 2:
        if ("--verbose" in sys.argv):
            exit_code = main(sys.argv[1], True)
            sys.exit(exit_code)
        print(f"Prompt argument was expected, but {len(sys.argv) - 1} arguments were given")
        sys.exit(1)

    exit_code = main(sys.argv[1])
    sys.exit(exit_code)
