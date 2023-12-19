
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    msg = [f"'{k}': {v}" for k, v in response.items() if k != 'dominant_emotion']
    return f"For the given statement, the system response is {', '.join(msg)}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
