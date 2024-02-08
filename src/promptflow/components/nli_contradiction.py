from sentence_transformers import CrossEncoder
from typing import List
from promptflow import tool

global nli_contradiction_model
nli_contradiction_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')

# TODO - implement nli_contradiction outside of the SelfCheck GPT framework

@tool
def compute_metric(context: str, response: str) -> List:
    
    nli_scores = nli_contradiction_model.predict([context, response])
    scores = nli_contradiction_model.predict([('A man is eating pizza', 'A man eats something'), ('A black race car starts up in front of a crowd of people.', 'A man is driving down a lonely road.')])

    print(nli_scores)
    print(scores)
    return

# Unit test
if __name__ == "__main__":
    context = "Faraday discovered electricity."
    response = "Faraday invented electricity."
    print(compute_metric(context, response))