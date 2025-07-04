
from transformers import  AutoTokenizer, AutoModelForCausalLM
from helpers import get_settings

class LoadModel: 
    def __init__(self):
        pass

    def load_tokenizer(self):
        settings = get_settings()
        
        # Load the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            settings.hugging_face_model,
            token=settings.hugging_face_api_key,
            trust_remote_code=True)
        return tokenizer
    
    def load_model(self):
        settings = get_settings()
        
        # Load the model
        model = AutoModelForCausalLM.from_pretrained(
            settings.hugging_face_model,
            low_cpu_mem_usage=True,
            torch_dtype="auto",
            token=settings.hugging_face_api_key,
            trust_remote_code=True
        )
        
        return model