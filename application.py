from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

# Load model and vectorizer
loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)

@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']  # Expecting JSON payload with 'text' key
    transformed_text = vectorizer.transform([text])
    prediction = loaded_model.predict(transformed_text)[0]

    # Return a JSON response
    response = 'REAL' if prediction == 1 else 'FAKE',  # Assuming 1 is for REAL and 0 is for FAKE

    print(response)
    print(response[0])

    jsonres = {"res": response[0]}

    print(jsonres)
    print(jsonify(jsonres))
    return jsonify(jsonres)

#jsonify({'prediction': prediction})
@application.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=5000)