import requests
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

# URL of the deployed API
API_URL = "http://test3-env.eba-y2knhxz7.us-east-2.elasticbeanstalk.com/predict"

# Sample news articles
test_cases = [
    "NASA's Mars rover has made a significant discovery.",  # Real news
    "The stock market hit a record high this week.",         # Real news
    "The moon is made of cheese.",                             # Fake news
    "Aliens have landed in New York City."                    # Fake news
]

# Create CSV file to log timestamps
csv_file = 'latency_results.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Test Case', 'Timestamp'])

    for news in test_cases:
        latencies = []
        for _ in range(100):  # 100 calls
            start_time = time.time()
            response = requests.post(API_URL, json={'text': news})
            latency = time.time() - start_time
            latencies.append(latency)
            writer.writerow([news, latency])

        # Calculate average latency
        average_latency = np.mean(latencies)
        print(f"Average latency for '{news}': {average_latency:.4f} seconds")

# Generate plot
plt.boxplot([latencies for _ in test_cases], labels=test_cases)
plt.ylabel('Latency (seconds)')
plt.title('Latency of Predictions for Different Test Cases')
plt.savefig('latency_boxplot.png')
plt.show()
