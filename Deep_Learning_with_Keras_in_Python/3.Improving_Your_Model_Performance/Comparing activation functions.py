'''
Comparing activation functions involves a bit of coding, but nothing you can't do!

You will try out different activation functions on the multi-label model you built for your irrigation machine in chapter 2. The function get_model() returns a copy of this model and applies the activation function, passed on as a parameter, to its hidden layer.

You will build a loop that goes through several activation functions, generates a new model for each and trains it. Storing the history callback in a dictionary will allow you to compare and visualize which activation function performed best in the next exercise!

'''


# Set a seed
np.random.seed(27)

# Activation functions to try
activations = ['relu','leaky_relu','sigmoid','tanh']

# Loop over the activation functions
activation_results = {}

for act in activations:
  # Get a new model with the current activation
  model = get_model(act)
  # Fit the model
  history = model.fit(X_train, y_train,
                      validation_data=(X_test, y_test),
                      epochs=20, verbose=0)
  activation_results[act] = history