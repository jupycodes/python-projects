#%%
import numpy as np
from numpy.lib.polynomial import polyfit
from numpy.random.mtrand import random_integers

class NeuralNetwork:
    def __init__(self, learning_rate):
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bias = np.random.randn()
        self.learning_rate = learning_rate
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_deriv(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))

    def predict(self, input_vector):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self.sigmoid(layer_1)
        prediction = layer_2
        return prediction

    def compute_gradients(self, input_vector, target):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self.sigmoid(layer_1)
        prediction = layer_2

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer_1 = self.sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

        derror_dbias = derror_dprediction * dprediction_dlayer_1 * dlayer1_dbias
        derror_dweights = derror_dprediction*dprediction_dlayer_1*dlayer1_dweights
        return derror_dbias, derror_dweights

    def update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (derror_dweights * self.learning_rate)

    def train(self, input_vectors, targets, iterations):
        cumulative_errors = []
        for current_iteration in range(iterations):
            randome_data_index = np.random.randint(len(input_vectors))

            input_vector = input_vectors[randome_data_index]
            target = targets[randome_data_index]

            derror_dbias, derror_dweights = self.compute_gradients(input_vector,target)

            self.update_parameters(derror_dbias,derror_dweights)

            if current_iteration % 100 == 0:
                cumulative_error = 0
                for data_instance_index in range(len(input_vectors)):
                    data_point = input_vectors[data_instance_index]
                    target = targets[data_instance_index]

                    prediction = self.predict(data_point)
                    error = np.square(prediction - target)

                    cumulative_error += error
                cumulative_errors.append(cumulative_error)
        return cumulative_errors
    
import matplotlib.pyplot as plt 

input_vectors = np.array([[3,1.5],[2,1],[4,1.5],[3,4],[3.5,0.5],[2,0.5],[5.5,1],[1,1]])
targets = np.array([0,1,0,1,0,1,1,0])
learning_rate = 0.1

neural_network = NeuralNetwork(learning_rate)
training_error = neural_network.train(input_vectors, targets, 10000)

plt.plot(training_error)
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
# %%
