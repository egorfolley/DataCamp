'''
You're going to train your first model in this course, and for a good cause!

Remember that before training your Keras models you need to compile them. This can be done with the .compile() method. The .compile() method takes arguments such as the optimizer, used for weight updating, and the loss function, which is what we want to minimize. Training your model is as easy as calling the .fit() method, passing on the features, labels and number of epochs to train for.

The model you built in the previous exercise is loaded for you to use, along with the time_steps and y_positions data.

'''


# Compile your model
model.compile(optimizer='adam', loss='mse')

print("Training started..., this can take a while:")

# Fit your model on your data for 30 epochs
model.fit(time_steps, y_positions, epochs=30)

# Evaluate your model 
print("Final lost value:",model.evaluate(time_steps, y_positions))
