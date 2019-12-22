#-----------------
#perceptrons
#
#
#------------------
import numpy as np



#variables

class perceptron:
    
    def __init__(self,nb_entre,nb_interm,name):

        self.w1=np.zeros((nb_entre,nb_interm))
        self.w2= np.zeros(nb_interm)
        self.b= np.zeros(nb_interm)
        self.name= name
        self.f= lambda x: 1/(1+ exp(-x))


        
    def give_predict(self,X):
        if len(X) == self.len:
            somme= self.w @ X
            print("somme= ",somme)
            y=self.f(somme)
            return y
        else:
            print("wrong length for X")
        
    def train1(self,X,true_y):
        if true_y!= self.give_predict(X):
            print("false y, current w= ",self.w)
            self.back_prop(X,true_y)
            print("false new w= ",self.w)
            return False
        else:
            print("NN guessed true y")
            return True
    
    def back_prop(self,X,true_y):
        self.w+= np.dot(true_y,X)
    
    def multi_training(self,train_set,max_wait,max_it):
        it=0
        
        while it<max_it:
            it+=1
            guesses=0
            train_set= random.shuffle(train_set)
            print("train_set= ",train_set)
            
            for i in range(len(train_set)):
                self.train1(train_set[i][0])
                
            for i in range(len(train_set)):
                if self.give_predict(train_set[i][0])==train_set[i][1]:
                    guesses+=1
            
                
        
        
        

    
      
perc1= perceptron(5,"1")
X= np.array((1,0,0,0,1))
print("X= ",X)
print("w= ",perc1.w)
print("y= ",perc1.give_predict(X))
print(perc1.train1(X,-1))

