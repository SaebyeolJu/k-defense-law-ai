from llama_index.readers import SimpleDirectoryReader
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "MLP-KTLim/llama-3-Korean-Bllossom-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

pipeline = transformers.pipeline(
    "text-generation",
    model=model_name,
    tokenizer=tokenizer,
    max_length=2048,
    temperature=0,
    top_p=0.95,
    repetition_penalty=1.15
)   

pipeline.model.eval()

