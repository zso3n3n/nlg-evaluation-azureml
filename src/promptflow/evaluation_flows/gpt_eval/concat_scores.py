from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(question: str, response: str, coherence: str, relevance: str, fluency: str) -> dict:

    output_json = {'question': question,
                   'response': response,
                   'gpt_relevance': relevance,
                   'gpt_fluency': fluency,
                   'gpt_coherence': coherence
                   }
    
    return output_json
