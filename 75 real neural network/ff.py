import numpy as np
from matplotlib import pyplot as plt
import random

class ffNet:
    def __init__(self,layers):
        self.layers = layers
        self.weights = self.genWeights()

        print([a.shape for a in self.weights])
        self.biases = self.genBiases()
        self.learnRate = 0.05


    def sigmoid(self,vals):
        return 1/(1+np.exp(-1*vals))

    def derSig(self,vals):
        return np.multiply(self.sigmoid(vals),(1-self.sigmoid(vals)))

    def feedForward(self,inputs):
        self.outputs=[]
        self.inputs=[]
        current = np.copy(inputs)
        self.outputs.append(np.copy(current))
        for layer,bias in zip(self.weights,self.biases):

            current = np.dot(layer,current)
            current = np.add(current,bias)
            self.inputs.append(np.copy(current))
            current = self.sigmoid(current)
            self.outputs.append(np.copy(current))
        return current

    def genWeights(self):
        return [np.random.rand(self.layers[iv+1],v) for iv,v in enumerate(self.layers[:-1])]

    def genBiases(self):
        return [np.random.rand(v) for v in self.layers[1:]]

    def totalError(self,i,desired):
        self.feedForward(i)
        return np.sum(np.divide(np.square(desired-self.outputs[-1]),2))

    def train(self,inp,out,printout=True):
        if len(inp) != len(out):
            raise ValueError("Training data doesn't match")
        count=0
        l=len(inp)
        for i,o in zip(inp,out):
            count+=1
            self.feedForward(i)
            if count%100==0 and printout:
                print("Error: {}       {}/{}".format(self.totalError(i,o),count,l))
            self.backPropagate(o)


    def backPropagate(self,desired):
        deltas = [0 for i in self.layers[1:]]
        deltas[-1] = np.multiply(
                                self.outputs[-1]-desired,
                                self.derSig(self.inputs[-1])
                                )

        for layer in range(len(deltas)-2,-1,-1):
            deltas[layer] = np.multiply(
                                        np.dot(self.weights[layer+1].T,deltas[layer+1]),
                                        self.derSig(self.inputs[layer])
                                        )

        for index in range(len(self.weights)):
            partial = np.outer(deltas[index],self.outputs[index])
            self.weights[index] = self.weights[index]-self.learnRate*partial

        for index in range(len(self.biases)):
            self.biases[index] = self.biases[index]-self.learnRate*deltas[index]

    def predict(self,inp):
        a = self.feedForward(inp)
        out = [1 if val>0.5 else 0 for val in a]
        return out
