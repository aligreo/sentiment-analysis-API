
from fastapi import APIRouter
from helpers import get_settings
from helpers import APIStandardFormat   
from utils import LoadModel
from datetime import datetime


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api","data"],
)

@data_router.post("/process")
async def process_data(data: APIStandardFormat):
    settings = get_settings()

    model = LoadModel().load_model()
    tokenizer = LoadModel().load_tokenizer()

    messages = [{'role':'system', 'system':settings.SYSTEM_PROMPT},
                {'role':'user', 'content':data.text}]
    ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        return_dict=True,
        add_generation_prompt=True,
        return_tensors="pt"
    )

    generated_ids = model.generate(
        **ids,
        max_new_tokens=4090,
        pad_token_id=tokenizer.eos_token_id
        )
    output = tokenizer.decode(generated_ids[0][len(ids['input_ids'][0]):], skip_special_tokens=True)

    return {"time":datetime.now(),
             "output": output
             }