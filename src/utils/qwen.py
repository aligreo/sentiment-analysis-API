from .load_model import LoadModel
from helpers import get_settings
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
from helpers.api_standard_format import APIStandardFormat   



model = LoadModel().load_model()
tokenizer = LoadModel().load_tokenizer()


def generate_with_qwen(prompt:str):

    settings = get_settings()

    messages = [
        {"role": "system", "content": settings.SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]

    ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        return_dict=True,
        add_generation_prompt=True,
        return_tensors="pt",
        enable_thinking=False
    )

    generated_ids = model.generate(
        **ids,
        max_new_tokens=4090,
        pad_token_id=tokenizer.eos_token_id
        )
    output = tokenizer.decode(generated_ids[0][len(ids['input_ids'][0]):], skip_special_tokens=True)

    return output