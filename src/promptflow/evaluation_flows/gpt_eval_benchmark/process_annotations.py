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
    for i in expert:
        expert_coherence += i['coherence']

    for i in turker:
        turker_coherence += i['coherence']
    
    output_json = {'expert': round(expert_coherence / len(expert),0),
                   'turk': round(turker_coherence / len(turker),0)
                   }
    
    return output_json


if __name__ == "main":
    annotations = "[{\"coherence\": 5, \"consistency\": 5, \"fluency\": 5, \"relevance\": 2}, {\"coherence\": 5, \"consistency\": 5, \"fluency\": 5, \"relevance\": 3}, {\"coherence\": 4, \"consistency\": 5, \"fluency\": 5, \"relevance\": 3}], \"turker_annotations\": [{\"coherence\": 2, \"consistency\": 2, \"fluency\": 1, \"relevance\": 2}, {\"coherence\": 5, \"consistency\": 4, \"fluency\": 5, \"relevance\": 3}, {\"coherence\": 4, \"consistency\": 1, \"fluency\": 5, \"relevance\": 1}, {\"coherence\": 3, \"consistency\": 4, \"fluency\": 4, \"relevance\": 3}, {\"coherence\": 4, \"consistency\": 4, \"fluency\": 4, \"relevance\": 4}]"
    result = process_annotations(annotations)
    print(result)