import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    dict_response = json.loads(response.text)
    emotion_list = dict_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_list['anger']
    disgust_score = emotion_list['disgust']
    fear_score = emotion_list['fear']
    joy_score = emotion_list['joy']
    sadness_score = emotion_list['sadness']
    dominant_emotion_score = max(emotion_list.values())
    dominant_emotion = ''

    for k, v in emotion_list.items():
        if v == dominant_emotion_score:
            dominant_emotion = k
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant emotion': f'{dominant_emotion}'
    }