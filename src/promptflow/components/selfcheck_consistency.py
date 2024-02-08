from selfcheckgpt.modeling_selfcheck import SelfCheckLLMPrompt
from promptflow import tool
from typing import List
import torch 

global device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

global llm_model
llm_model = "mistralai/Mistral-7B-Instruct-v0.2"

@tool
def compute_metric(sentences: List, samples: List) -> List:
    selfcheck_prompt = SelfCheckLLMPrompt(llm_model, device)
    sent_scores_prompt = selfcheck_prompt.predict( sentences = sentences, sampled_passages = samples)
    
    return sent_scores_prompt # could take the max value here to detect ANY hallucination