from promptflow import tool

@tool
def process_results(cot_result: str) -> int:
    
    if cot_result.lower() == "yes":
        return 1
    elif cot_result.lower() == "no":
        return 0
    else:
        return -1
