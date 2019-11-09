'''
The history callback is returned by default every time you train a model with the .fit() method. To access these metrics you can access the history dictionary inside the returned callback object and the corresponding keys.

The irrigation machine model you built in the previous lesson is loaded for you to train, along with its features and labels (X and y). This time you will store the model's historycallback and use the validation_data parameter as it trains.

You will plot the results stored in history with plot_accuracy() and plot_loss(), two simple matplotlib functions. You can check their code in the console by typing print(inspect.getsource(plot_loss)).

Let's see the behind the scenes of our training!

'''


# Train your model and save it's history
history = model.fit(X_train, y_train, epochs = 50,
               validation_data=(X_test, y_test))

# Plot train vs test loss during training
plot_loss(history.history['loss'], history.history['val_loss'])

# Plot train vs test accuracy during training
plot_accuracy(history.history['acc'], history.history['val_acc'])