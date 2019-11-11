'''
The code used in the previous exercise has been executed to obtain theactivation_results with the difference that 100 epochs instead of 20 are used. That way you'll have more epochs to further compare how the training evolves per activation function.

For every history callback of each activation function in activation_results:

The history.history['val_loss'] has been extracted.
The history.history['val_acc'] has been extracted.
Both are saved in two dictionaries: val_loss_per_function and val_acc_per_function.
Pandas is also loaded for you to use as pd. Let's plot some quick comparison validation loss and accuracy charts with pandas!

'''


# Create a dataframe from val_loss_per_function
val_loss=pd.DataFrame(val_loss_per_function)

# Call plot on the dataframe
val_loss.plot()
plt.show()

# Create a dataframe from val_acc_per_function
val_acc = pd.DataFrame(val_acc_per_function)

# Call plot on the dataframe
val_acc.plot()
plt.show()