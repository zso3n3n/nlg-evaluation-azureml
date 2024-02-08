from sentence_transformers import CrossEncoder
from promptflow import tool

global hallucination_model
hallucination_model = CrossEncoder('vectara/hallucination_evaluation_model')

@tool
def compute_metric(context: str, response: str) -> float:
    hallucination_score = hallucination_model.predict([context, response])
    return hallucination_score
