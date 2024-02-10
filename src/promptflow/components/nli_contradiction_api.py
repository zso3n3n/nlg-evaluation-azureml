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
    response = urllib.request.urlopen(req)

    result = response.read()
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
    deployment_name = "cross-encoder-nli-deberta-v3--6" # add deployment name here

    api_key="qiIOwKrpRcqN1VLSaLJ4JUz7G2u6JfOr"
    url="https://nlg-eval-aml-rndvt.centralus.inference.ml.azure.com/score"

    # Prepare header
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': f'{deployment_name}'}

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
    nli_zipped = dict(zip(data['labels'], data['scores']))

    return nli_zipped['contradiction']

if __name__ == "__main__":
    response = "Faraday did not discover electricity"
    context = "Electricity was discovered by Faraday."
    score_results = compute_nli_scores(response, context)
    print(score_results)
