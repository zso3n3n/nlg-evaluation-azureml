from selfcheckgpt.modeling_selfcheck import SelfCheckLLMPrompt
from promptflow import tool
from typing import List
import torch 

global device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

global llm_model
llm_model = "mistralai/Mistral-7B-Instruct-v0.2"

# TODO: Maybe a bug in SelfCheck GPT? This code does not work.

@tool
def compute_metric(sentences: List, samples: List) -> List:
    selfcheck_prompt = SelfCheckLLMPrompt(llm_model, device)
    sent_scores_prompt = selfcheck_prompt.predict( sentences = sentences, sampled_passages = samples)
    
    return sent_scores_prompt # could take the max value here to detect ANY hallucination

# Unit test
if __name__ == "__main__":

    sentences = ['Michael Alan Weiner (born March 31, 1942) is an American radio host.', 'He is the host of The Savage Nation.']

    sample1 = "Michael Alan Weiner (born March 31, 1942) is an American radio host. He is the host of The Savage Country."
    sample2 = "Michael Alan Weiner (born January 13, 1960) is a Canadian radio host. He works at The New York Times."
    sample3 = "Michael Alan Weiner (born March 31, 1942) is an American radio host. He obtained his PhD from MIT."
    samples = [sample1,sample2, sample3]

    print(compute_metric(sentences, samples))