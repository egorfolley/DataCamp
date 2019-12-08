'''
Training a CNN with pooling layers is very similar to training of the deep networks that y have seen before. Once the network is constructed (as you did in the previous exercise), the model needs to be appropriately compiled, and then training data needs to be provided, together with the other arguments that control the fitting procedure.

The following model from the previous exercise is available in your workspace:

Convolution => Max pooling => Convolution => Flatten => Dense

'''


# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Fit to training data
model.fit(train_data, train_labels, epochs=3, 
            batch_size=10, validation_split=.2)

# Evaluate on test data 
model.evaluate(test_data, test_labels, batch_size=10)