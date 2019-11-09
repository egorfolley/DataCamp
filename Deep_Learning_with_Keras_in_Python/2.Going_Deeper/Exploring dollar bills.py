'''
You will practice building classification models in Keras with the Banknote Authentication dataset.

Your goal is to distinguish between real and fake dollar bills. In order to do this, the dataset comes with 4 variables: variance,skewness,curtosis and entropy. These variables are calculated by applying mathematical operations over the dollar bill images. The labels are found in the class variable.


The dataset is pre-loaded in your workspace as banknotes, let's do some data exploration!

'''


# Import seaborn
import seaborn as sns

# Use pairplot and set the hue to be our class
sns.pairplot(banknotes,hue="class") 

# Show the plot
plt.show()

# Describe the data
print('Dataset stats: \n', banknotes.describe())

# Count the number of observations of each class
print('Observations per class: \n', banknotes["class"].value_counts())