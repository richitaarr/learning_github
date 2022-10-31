import tensorflow as tf

def predict(input):
    model = tf.load('...')
    y = model.fit(input)
    return y
