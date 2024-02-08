from promptflow import tool
from typing import List

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(response: str, context: str, samples: List, hhem_score: float, sent_scores_nli: List, consistency_score: List, chain_poll_score: float, human_label: int) -> dict:

    output_json = {'response': response,
                   'samples': samples,
                   'context': context,
                   'hhem_score': hhem_score,
                   'nli_contradiction': sent_scores_nli,
                   'consistency' : consistency_score,
                   'chain_poll' : chain_poll_score
                   }
    
    return output_json
