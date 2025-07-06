
from datasets import load_dataset

class ImdbDataset:
    def __init__(self, dataset_name: str, split:str):
        self.dataset_name = dataset_name
        self.split = None

    def load_data(self):
        if self.split:
            dataset = load_dataset(self.dataset_name, split=self.split)
            return dataset
        else:
            dataset = load_dataset(self.dataset_name)
            return dataset

