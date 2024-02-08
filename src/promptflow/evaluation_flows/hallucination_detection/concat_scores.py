from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(question: str, answer: str, context: str, groundedness_answer: str, goundedness_question: str, question_context_sim: float, answer_context_sim: float) -> dict:

    output_json = {'question': question,
                   'answer': answer,
                   'context': context,
                   'groundedness_answer': groundedness_answer,
                   'goundedness_question': goundedness_question,
                   'question_context_sim' : question_context_sim,
                   'answer_context_sim' : answer_context_sim
                   }
    
    return output_json
