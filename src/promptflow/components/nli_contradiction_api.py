import urllib.request
import json
import os
import ssl
import requests
import ast
from promptflow import tool


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def make_request(body, url, headers):
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
    
    return result

def decode_result(result):
    dict_str = result.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    return mydata

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

@tool
def compute_nli_scores(response: str, context: str) -> float:
    
    # get configs
    url = os.environ.get("DEBERTA_API_BASE")
    api_key = os.environ.get('DEBERTA_API_KEY')

    # Prepare header
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'ce-nli-deberta-v3-small'}

    # Prepare body
    data ={
            "inputs": f"{response} {context}",
            "parameters": {"candidate_labels": ["entailment","contradiction"]},
            }

    body = str.encode(json.dumps(data))

    # Make Request
    result = make_request(body, url, headers)

    # Decode and Process Response
    data = decode_result(result)
    nli_score = data['scores'][0]

    return nli_score

if __name__ == "__main__":
    response = "Faraday did not discover electricity"
    context = "Electricity was discovered by Faraday."
    compute_nli_scores(response, context)