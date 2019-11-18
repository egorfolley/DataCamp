'''
Your LSTM model has already been trained for you so that you don't have to wait. It's time to define a function that decodes its predictions.

Since you are predicting on a model that uses the softmax function,argmax() is used to obtain the position of the output layer with the highest probability, that is the index representing the most probable next word.

The tokenizer you previously created and fitted, is loaded for you. You will be making use of its internal index_word dictionary to turn the model's next word prediction (which is an integer) into the actual written word it represents.

You're very close to experimenting with your model!

'''


def predict_text(test_text):
  if len(test_text.split())!=3:
    print('Text input should be 3 words!')
    return False
  
  # Turn the test_text into a sequence of numbers
  test_seq = tokenizer.texts_to_sequences([test_text])
  test_seq = np.array(test_seq)
  
  # Get the model's next word prediction by passing in test_seq
  pred = model.predict(test_seq).argmax(axis = 1)[0]
  
  # Return the word associated to the predicted index
  return tokenizer.index_word[pred]