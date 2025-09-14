import requests

def sentiment_analyzer(text_to_analyze):
    ''' This function takes the input text and applies sentiment analysis
        over it using the deployed model on IBM Cloud. The output returns
        the sentiment label and its confidence score.
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        formatted_response = response.json()
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    if response.status_code == 500:
        label = None
        score = None
    
    return {'label': label, 'score': score}
