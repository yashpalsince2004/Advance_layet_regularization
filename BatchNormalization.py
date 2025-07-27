import tensorflow as tf
from tensorflow.keras.layers import BatchNormalization

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    BatchNormalization(),
    tf.keras.layers.Dense(10, activation='softmax')
])
