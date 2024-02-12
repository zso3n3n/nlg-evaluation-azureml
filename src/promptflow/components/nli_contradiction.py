from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import List
from promptflow import tool
import numpy as np

# TODO - this is the easiest implementation of nli_contradiction score. But it crashes the kernel every time...


global model
model = AutoModelForSequenceClassification.from_pretrained('cross-encoder/nli-deberta-v3-small')

global tokenizer
tokenize = AutoTokenizer.from_pretrained('cross-encoder/nli-deberta-v3-small', use_fast=False)

@tool
def compute_metric(context: str, response: str) -> int:

    features = tokenizer([response],[context],  padding=False, truncation=False, return_tensors="pt")

    model.eval()
    with torch.no_grad():
        scores = model(**features).logits
        # print(scores)

    # the nli-deberta-v3-base model outputs 3 scores in a list. The index of the list represents the following:
    # 0: contradiction, 1: entailment, 2: neutral
    # The maximum score is the model's prediction, we use the argmax function to get the index of the maximum score
    result = np.argmax(scores)
    if result == 0:
        return 1
    else:
        return 0

# Unit test
if __name__ == "__main__":
    context = "Faraday discovered electricity."
    response = "Faraday invented electricity."
    print(compute_metric(context, response))