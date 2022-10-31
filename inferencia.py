import tensorflow as tf
import pandas as pd

def input_fn(data, content_type):
    if content_type == 'json':
        data = pd.read_json(data)
    return data
    
def predict(input):
    model = tf.load('...')
    y = model.fit(input)
    return y
