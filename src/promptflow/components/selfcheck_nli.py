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
    
    return round(max(sent_scores_nli),2) # take the max value here to detect ANY hallucination

# Unit test
if __name__ == "__main__":

    sentences = ['Michael Alan Weiner (born March 31, 1942) is an American radio host.', 'He is the host of The Savage Nation.']

    sample1 = "Michael Alan Weiner (born March 31, 1942) is an American radio host. He is the host of The Savage Country."
    sample2 = "Michael Alan Weiner (born January 13, 1960) is a Canadian radio host. He works at The New York Times."
    sample3 = "Michael Alan Weiner (born March 31, 1942) is an American radio host. He obtained his PhD from MIT."
    samples = [sample1,sample2, sample3]

    print(compute_metric(sentences, samples))