from promptflow import tool
import json
from typing import List

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def process_annotations(expert: List[dict], turker: List[dict]) -> dict:
    expert_coherence = 0
    turker_coherence = 0
    for e in expert:
        expert_coherence += e['coherence']

    for t in turker:
        turker_coherence += t['coherence']
    
    output_json = {'expert': round(expert_coherence/3, 0),
                   'turk': round(turker_coherence/5, 0)
                   }
    
    return output_json