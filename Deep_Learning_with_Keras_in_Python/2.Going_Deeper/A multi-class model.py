'''
You're going to build a model that predicts who threw which dart only based on where that dart landed! (That is the dart's x and y coordinates.)

This problem is a multi-class classification problem since each dart can only be thrown by one of 4 competitors. So classes are mutually exclusive, and therefore we can build a neuron with as many output as competitors and use the softmax activation function to achieve a total sum of probabilities of 1 over all competitors.

Keras Sequential model and Dense layer are already loaded for you to use.

'''


# Instantiate a sequential model
model = Sequential()
  
# Add 3 dense layers of 128, 64 and 32 neurons each
model.add(Dense(128, input_shape=(2,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
  
# Add a dense layer with as many neurons as competitors
model.add(Dense(4, activation="softmax"))
  
# Compile your model using categorical_crossentropy loss
model.compile(loss="categorical_crossentropy",
              optimizer='adam',
              metrics=['accuracy'])