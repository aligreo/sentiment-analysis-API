
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import Trainer, TrainingArguments
from data_loader import Dataset
from helpers import get_settings
import numpy as np
import torch
import evaluate

settings = get_settings()


model = AutoModelForSequenceClassification.from_pretrained(settings.HUGGING_FACE_MODEL,
                                                           torch_dtype=torch.float16,
                                                           trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(settings.HUGGING_FACE_MODEL,
                                          trust_remote_code=True)


dataset = Dataset(dataset_name='imdb', split='train').load_data()

def process_dataset(row):
    return tokenizer(row['text'], padding=True, truncation=True)


processed_dataset = dataset.map(
    process_dataset,
    batched=True
)

acc = evaluate.load("accuracy")

def accuracy_metric(model_outputs):
    logits, labels = model_outputs
    predictions = np.argmax(logits, axis=1)
    return acc.compute(predictions=predictions, references=labels)

splitted_dataset = processed_dataset.train_test_split(test_size=0.2)

def train_model():

    training_args = TrainingArguments(
        output_dir='./model_development/finetuned_bert_model_imdb_dataset',
        num_train_epochs=3,
        per_device_train_batch_size=4,
        per_dvevice_eval_batch_size=4,
        learning_rate=2e-5,
        optimizer='adamw_torch',
        lr_scheduler_type='linear',
        warmup_ratio=0.1,
        weight_decay=0.01,
        logging_steps=100,
        save_total_limit=2,
        evaluation_strategy="epoch",
        logging_dir='./model_development/logs',
        report_to="none",
        run_name='finetuned_bert_model_imdb_dataset',
    )

    trainer = Trainer(
        model=model,
        processing_class=tokenizer,
        args=training_args,
        train_dataset=processed_dataset['train'],
        eval_dataset=splitted_dataset['test'],
        comupute_metrics=accuracy_metric,
    )

    trainer.train()

    return trainer

trainer = train_model()