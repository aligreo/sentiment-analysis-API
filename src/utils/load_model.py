
from transformers import  AutoTokenizer, AutoModelForCausalLM
from helpers import get_settings
import torch

class LoadModel: 
    def __init__(self):
        self.settings = get_settings()

    def load_tokenizer(self):
        
        # Load the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            self.settings.hugging_face_model,
            token=self.settings.hugging_face_api_key,
            trust_remote_code=True)
        return tokenizer
    
    def load_model(self):
        settings = get_settings()
        
        # Load the model
        model = AutoModelForCausalLM.from_pretrained(
            self.settings.hugging_face_model,
            torch_dtype=torch.float16,
            token=self.settings.hugging_face_api_key,
            trust_remote_code=True
        )
        
        return model