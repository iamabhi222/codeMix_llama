from transformers import AutoTokenizer
from huggingface_hub import login

login(token = '--key--')

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
text = "Write your text here"
tokens = tokenizer.tokenize(text)
num_tokens = len(tokens)
print(f"Number of tokens in your text: {num_tokens}")