from selfcheckgpt.modeling_selfcheck import SelfCheckNLI
from promptflow import tool
from typing import List
import torch 

global device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@tool
def compute_metric(sentences: List, samples: List) -> List:
    selfcheck_nli = SelfCheckNLI(device=device) # set device to 'cuda' if GPU is available
    sent_scores_nli = selfcheck_nli.predict(sentences = sentences, sampled_passages = samples)
    
    return sent_scores_nli # could take the max value here to detect ANY hallucination
