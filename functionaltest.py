import unittest
import json
import requests

API_URL_TEST = "http://test3-env.eba-y2knhxz7.us-east-2.elasticbeanstalk.com"
API_URL = "http://test3-env.eba-y2knhxz7.us-east-2.elasticbeanstalk.com/predict"

class FlaskAppTests(unittest.TestCase):
    
    def test_predict_news(self):
        real_news_samples = [
            "NASA's Mars rover has made a significant discovery.",
            "The stock market hit a record high this week."
        ]
        for news in real_news_samples:
            response = requests.post("http://test3-env.eba-y2knhxz7.us-east-2.elasticbeanstalk.com/predict", json={'text': news})
            json_response = response.json()
        
            self.assertEqual(response.status_code, 200)
            
            #print(json_response["res"])
            var = json_response["res"]

            self.assertEqual(var,'FAKE')  # Assuming 1 indicates real news
        
        fake_news_samples = [
            "The moon is made of cheese.",
            "Aliens have landed in New York City."
        ]
        for news in fake_news_samples:
            response = requests.post("http://test3-env.eba-y2knhxz7.us-east-2.elasticbeanstalk.com/predict", json={'text': news})
            json_response = response.json()
        
            self.assertEqual(response.status_code, 200)
            
            #print(json_response["res"])
            var = json_response["res"]

            self.assertEqual(var, 'FAKE')  # Assuming 1 indicates real news


if __name__ == '__main__':
    unittest.main()