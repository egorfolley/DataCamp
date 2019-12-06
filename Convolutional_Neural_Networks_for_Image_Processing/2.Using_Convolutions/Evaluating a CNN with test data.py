'''
To evaluate a trained neural network, you should provide a separate testing data set of labeled images. The model you fit in the previous exercise is available in your workspace.

'''


# Evaluate the model on separate test data
model.evaluate(test_data, test_labels, batch_size=10)