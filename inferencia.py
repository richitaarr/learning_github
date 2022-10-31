import tensorflow as tf
import pandas as pd

def input_fn(data, content_type):
    if content_type == 'json':
        data = pd.read_json(data)
    return data

def model_fn(dir):
    model = tf.load_model(dir)
    return model

def predict(model, input):
    y = model.fit(input)
    return y
