import numpy

def sigmoid(x):
	den = 1.0 + e ** (-1.0 * x)
	d = 1.0 / den
	return d

class Neuron:
	def __init__(self, weights):
		self.weights = weights
		self.values = [0] * len(self.weights)
		self.val = 0
		self.inputs = [0] * len(self.weights)
	
	def feed(self, values, bias):
		self.values = values
		self.val = 0
		self.inputs = values
		for i in range(len(self.weights) - 1):
			self.val += self.weights[i] * self.values[i]
		self.val += bias * self.weights[-1]
	
	def getVal(self, transfunc):
		return transfunc(self.val)

class NeuralNetwork:
	def __init__(self, layers, transfunc):
		self.layers = layers
		self.transfunc = transfunc
		self.value = 0
		self.values = [0] * len(self.layers[0] - 1)
		self.inputs = [0] * len(self.values)
	
	def __init__(self, dimensions, transfunc):
		# The input neurons are not counted as objects. 
		layers = [0] * (len(dimensions) - 1)
		for i in range(len(layers)):
			# Make a neuron with weights per each previous layer
			p = Neuron(([0.5] * (dimensions[i])))
			# Set the layer to be however many neuron + bias
			layers[i] = [p] * (dimensions[i + 1] + 1)
			# Set bias
			layers[i][-1] = 0.5
		self.layers = layers
		self.transfunc = transfunc
		self.value = 0
		self.values = [0] * dimensions[0]
		self.inputs = [0] * len(self.values)

	def feedForward(self, values):
		self.values = values
		self.inputs = values
		# The last element is always the bias
		for i in range(len(self.layers[0]) - 1):
			self.layers[0][1].feed(values, self.layers[0][-1])
		for i in range(len(self.layers) - 1):
			# Get the outputs from the previous layer
			outputs = [0] * (len(self.layers[i]) - 1)
			for n in range(len(self.layers[i]) - 1):
				outputs[n] = self.layers[i][n].getVal(self.transfunc)
			# Feed the results to the next one
			for n in range(len(self.layers[i + 1]) - 1):
				self.layers[i + 1][n].feed(outputs, self.layers[i + 1][-1])
	
	def getVals(self):
		outputs = [0] * (len(self.layers[-1]) - 1)
		for n in range(len(self.layers[-1]) - 1):
			outputs[n] = self.layers[-1][n].getVal(self.transfunc)
		return outputs

	def batchGradDescent(self, alpha, targets):
		err = numpy.subtract(self.getVals(), targets)
		meanerr = 0
		for i in range(len(err)):
			meanerr += err[i]
		for row in range(len(self.layers)):
			for i in range(len(self.layers[row]) - 1):
				cneuron = self.layers[row][i]
				for w in range(len(cneuron.weights)):
					cneuron.weights[w] = cneuron.weights[w] - alpha * meanerr * cneuron.inputs[w]

	def string(self):
		string = ""
		for i in range(len(self.layers)):
			string += ("L{}: \n".format(i))
			for n in range(len(self.layers[i]) - 1):
				string += ("    W: {}\n".format(self.layers[i][n].weights))
			string += ("\n    B: {}\n".format(self.layers[i][-1]))
			
		return string

p = Neuron([0.32, 0.78])
p.feed([1.7, 0.8], 0.5)
ann = NeuralNetwork([3, 5, 2], numpy.sin)
ann.feedForward([5, 2, 0.1])
print("Result 1")
print(ann.getVals())
ann.batchGradDescent(0.1, [0.2, 0.5])
ann.feedForward([5, 2, 0.1])
print("Result 2")
print(ann.getVals())
ann.batchGradDescent(0.1, [0.2, 0.5])
ann.feedForward([5, 2, 0.1])
print("Result 3")
print(ann.getVals())
