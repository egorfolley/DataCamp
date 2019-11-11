'''
Time to train your model with the best parameters found: 0.001 for the learning rate, 50 epochs,a 128 batch_size and relu activations.

The create_model() function has been redefined so that it now creates a model with those parameters. X and y are loaded for you to use as features and labels.

In this exercise you do pass the best epochs and batchsize values found for your model to the KerasClassifier object so that they are used when performing crossvalidation.

End this chapter by training an awesome tuned model on the breast cancer dataset!

'''


# Import KerasClassifier from keras wrappers
from keras.wrappers.scikit_learn import KerasClassifier

# Create a KerasClassifier
model = KerasClassifier(build_fn = create_model, epochs = 50, 
             batch_size = 128, verbose = 0)

# Calculate the accuracy score for each fold
kfolds = cross_val_score(model, X, y, cv = 3)

# Print the mean accuracy
print('The mean accuracy was:', kfolds.mean())

# Print the accuracy standard deviation
print('With a standard deviation of:', kfolds.std())