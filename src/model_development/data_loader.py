
from datasets import load_dataset
from dataclasses import dataclass

@dataclass
class Dataset:
    dataset_name: str
    split: str = None

    def load_data(self):
        if self.split is not None:
            dataset = load_dataset(self.dataset_name, split=self.split)
            return dataset
        
        dataset = load_dataset(self.dataset_name)
        return dataset

