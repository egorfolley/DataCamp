'''
You are now ready to train your model and check how well it performs when classifying new bills! The dataset has already been partitioned as X_train, X_test,y_train and y_test

'''


# Train your model for 20 epochs
model.fit(X_train, y_train, epochs=20)

# Evaluate your model accuracy on the test set
accuracy = model.evaluate(X_test, y_test)[1]

# Print accuracy
print('Accuracy:', accuracy)