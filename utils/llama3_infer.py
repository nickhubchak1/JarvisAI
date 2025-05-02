from llama_cpp import Llama

llm = Llama(
    model_path="./models/llama-3-8b.gguf",
    n_ctx=2048,
    n_threads=4
)

def generate_response(prompt: str):
    output = llm(prompt, max_tokens=256, stop=["</s>"])
    return output["choices"][0]["text"].strip()
