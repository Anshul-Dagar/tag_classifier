from huggingface_hub import InferenceClient
import re
import json

repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

llm_client = InferenceClient(
    model=repo_id,
    timeout=500,

)

def generate_tags(inference_client: InferenceClient, title:str):
    try:
        response =inference_client.post(  
            json={
            "inputs": title,
            "parameters": {"max_new_tokens": 200},
            "task": "text-generation",
        },)
        # response.raise_for_status()
        generated_text = json.loads(response.decode())[0]["generated_text"]
        pattern = r'\b(\w+):'
        tags = re.findall(pattern, generated_text)
        # tags= generated_text.split()[:3]
        unique_tags =set(tags[1:10])
        print(generated_text) 
        print(unique_tags) 
    except Exception as e:
        print(f"Error generating tags: {str(e)}")
        return ["N/A", "N/A", "N/A"]
    
if __name__ == "__main__":
    generate_tags(llm_client, 'Linus Torvalds explains why aging Linux developers are a good thing')