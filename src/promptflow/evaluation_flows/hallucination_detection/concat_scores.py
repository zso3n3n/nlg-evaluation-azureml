from promptflow import tool
from typing import List

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(response: str, context: str, samples: List, hhem_score: float, nli_score: float, consistency_score: int, chain_poll_score: float, human_label: int) -> dict:

    output_json = {'response': response,
                   'samples': samples,
                   'context': context,
                   'hhem_score': hhem_score,
                   'nli_score': nli_score,
                   'consistency_score' : consistency_score,
                   'chain_poll' : chain_poll_score,
                   'human_label' : human_label,
                   }
    
    return output_json
