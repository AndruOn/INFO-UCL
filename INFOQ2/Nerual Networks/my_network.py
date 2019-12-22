#-------------
#Basic Neural Network 
#
#Andru Onciul
#--------------
import numpy as np

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))


class Network:
    
    def __init__(self, sizes,activation_function,test_on=False):
        """sizes are the sizes of each layer. ex:[4,3,1] is a neural
        network with an input layer of 4 neurones, a hidden layer of 3 neurones
        and a output layer of 1 neurone"
            """
        if test_on==False:
            self.sizes = sizes
            self.biases = np.array([np.random.rand(x) for x in sizes[1:]])
            self.weights = np.array([np.random.rand(x, y) for x, y in zip(sizes[:-1],sizes[1:])])
            self.f= activation_function
        else:
            self.sizes = sizes
            self.biases = np.array([np.ones(x) for x in sizes[1:]])
            self.weights = np.array([np.ones((x, y)) for x, y in zip(sizes[:-1],sizes[1:])])
            self.f= activation_function
        
    def __str__(self):
        s= "Neural network {0}\n".format(self.sizes)
        s+= "weights= {0} \n biases= {1}".format(self.weights,self.biases)
        return(s)
    
    def feedforward(self,a,print_on=False):
        """Returns the output of the Neural Network for a certain input a.
            """
        w = self.weights
        b = self.biases
        for i in range(len(self.sizes)-1):
            a = self.f(np.dot(a,w[i])+b[i])
            if print_on==True:
                print("i={0},\nw[{0}]={1},\nb[{0}]={2}".format(i,w[i],b[i]))
                print("a[{0}]= {1}".format(i,a))
        return a
        
    
    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        pass
    
    
    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        pass
    
    
    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
        is the learning rate."""
        pass
               
               
    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        pass
    
    
    def SGD(self, training_data, epochs, mini_batch_size, eta,test_data=None):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        pass
    
        
    
    
    
    
net= Network([4,3,1],sigmoid)
print(net)
print("output= ",net.feedforward((1,1,1,1),print_on=True))