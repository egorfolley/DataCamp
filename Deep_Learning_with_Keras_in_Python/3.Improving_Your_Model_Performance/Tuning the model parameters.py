'''
It's time to try out different parameters on your model and see how well it performs!

The create_model() function you built in the previous exercise is loaded for you to use.

Since fitting the RandomizedSearchCV would take too long, the results you'd get are printed in the show_results() function. You could try random_search.fit(X,y) in the console yourself to check it does work after you have built everything else, but you will probably timeout your exercise (so copy your code first if you try it!).

You don't need to use the optional epochs and batch_size parameters when building your KerasClassifier since you are passing them as params to the random search and this works as well.

'''


# Import KerasClassifier from keras wrappers
from keras.wrappers.scikit_learn import KerasClassifier

# Create a KerasClassifier
model = KerasClassifier(build_fn = create_model)

# Define the parameters to try out
params = {'activation': ['relu', 'tanh'], 'batch_size': [32,128, 256], 
          'epochs': [50, 100, 200], 'learning_rate': [.1,.01, .001]}

# Create a randomize search cv object passing in the parameters to try
random_search = RandomizedSearchCV(model, param_distributions = RandomizedSearchCV, cv = KFold(3))

# Running random_search.fit(X,y) would start the search,but it takes too long! 
show_results()