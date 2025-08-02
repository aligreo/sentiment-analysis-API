# sentiment-analysis-api using FastAPI framework.

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/945097c2-bb87-49f7-b3e8-e6e5dc98046d" />

<br><br>
to get start using this project and adjusting it you need to clone the project and install the required packages and start editing.

```bash

!pip install -r requirements.txt 

```

to get start loading any model from huggingface you only need to import the model and it's tokenizer

```bash
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = num_labels)

```
