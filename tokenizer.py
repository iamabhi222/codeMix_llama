from transformers import AutoTokenizer
from huggingface_hub import login

login(token = '--api--')

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-405B")
text = "he Telangana State Tourism Development Corporation is a state government agency that promotes tourism in Telangana."
tokens = tokenizer.tokenize(text)
num_tokens = len(tokens)
print(f"Number of tokens in your text: {num_tokens}")