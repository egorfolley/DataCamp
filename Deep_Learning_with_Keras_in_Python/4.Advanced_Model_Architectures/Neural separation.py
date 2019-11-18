'''
Neurons learn by updating their weights to output values that help them distinguish between the input classes. So put on your gloves because you're going to perform brain surgery!

You will make use of the inp_to_out() function you just built to visualize the output of two neurons in the first layer of the Banknote Authentication model as epochs go by. Plotting the outputs of both of these neurons against each other will show you the difference in output depending on whether each bill was real or fake.

The model you built in chapter 2 is ready for you to use, just like X_test and y_test. Copy print(inspect.getsource(plot)) in the console if you want to check plot().

You're performing heavy duty, once it's done, take a look at the graphs to watch the separation live!

'''


for i in range(0, 21):
  	# Train model for 1 epoch
    h = model.fit(X_train, y_train, batch_size=16, epochs=1,verbose=0)
    if i%4==0: 
      # Get the output of the first layer
      layer_output = inp_to_out([X_test])[0]
      
      # Evaluate model accuracy for this epoch
      test_accuracy = model.evaluate(X_test, y_test)[1] 
      
      # Plot 1st vs 2nd neuron output
      plot()