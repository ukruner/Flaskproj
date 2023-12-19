"""server.py file coordinates the routes and supports API calls"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """This decorator calls emotion_analyzer function as a response to /emotionDetector"""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    msg = [f"'{k}': {v}" for k, v in response.items() if k != 'dominant_emotion']
    return (f"For the given statement, the system response is {', '.join(msg)}." +
    "The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """renders main page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
