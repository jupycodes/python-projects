import numpy as np
input_vector_1 = np.array([1.66,1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0,0])

def sigmoid(x):
    return 1/(1+np.exp(-x))

def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2

#Example vector 1
prediction_1 = make_prediction(input_vector_1, weights_1, bias)
print(f"The prediction result is : {prediction_1}")

#Example vector 2
input_vector_2 = np.array([2,1.5])
weights_2 = np.array([1.45, -0.66])
prediction_2 = make_prediction(input_vector_2, weights_2, bias)
print(f"The prediction result is : {prediction_2}")

#reducing prediction error (example 2)
target = 0

def error_calc(prediction,target):
    mse = np.square(prediction - target)
    print(f"Prediction: {prediction}; Error: {mse}")

derivative = 2*(prediction_2 - target)
print(f"Derivative Ex 2 is: {derivative}")
weights_2 -= derivative
prediction_2 = make_prediction(input_vector_2, weights_2, bias)
error_calc(prediction_2, target)

#reducing prediction error (example 1) using same derivative
print(f"Derivative Ex 1 is: {derivative}")
weights_1 -= derivative
prediction_1 = make_prediction(input_vector_1, weights_1, bias)
error_calc(prediction_1, target)



