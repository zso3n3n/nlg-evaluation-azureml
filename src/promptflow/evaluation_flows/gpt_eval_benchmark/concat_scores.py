from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(response: str, coherence: str,coherence_w_emotion: str, human_coherence: dict) -> dict:

    output_json = {'response': response,
                   'gpt_coherence': int(coherence),
                   'gpt_coherence_w_emotion': int(coherence_w_emotion),
                   'expert_coherence': human_coherence['expert'],
                   'turker_coherence': human_coherence['turk']
                   }
    
    return output_json
