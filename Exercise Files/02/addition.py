import os
import tensorflow as tf

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 0: display all logs
# 1: filter out INFO logs
# 2: filter out WARNING logs
# 3: filter out ERROR logs

# Define computational graph
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='X')

addition = tf.add(X, Y, name='addition')

# Create the session
with tf.Session() as session:
    result = session.run(addition, feed_dict={X: [3, -23, 877, 14303], Y: [4, 0.00234, 1000, 21]})
    print(result)
