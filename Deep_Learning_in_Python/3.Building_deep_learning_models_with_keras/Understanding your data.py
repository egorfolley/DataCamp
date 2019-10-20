'''
You will soon start building models in Keras to predict wages based on various professional and demographic factors. Before you start building a model, it's good to understand your data by performing some exploratory analysis.

The data is pre-loaded into a pandas DataFrame called df. Use the .head() and .describe() methods in the IPython Shell for a quick overview of the DataFrame.

The target variable you'll be predicting is wage_per_hour. Some of the predictor variables are binary indicators, where a value of 1 represents True, and 0 represents False.

Of the 9 predictor variables in the DataFrame, how many are binary indicators? The min and max values as shown by .describe() will be informative here. How many binary indicator predictors are there?

'''


In [1]: df.head()
Out[1]: 
   wage_per_hour  union  education_yrs  experience_yrs  age  female  marr  \
0           5.10      0              8              21   35       1     1   
1           4.95      0              9              42   57       1     1   
2           6.67      0             12               1   19       0     0   
3           4.00      0             12               4   22       0     0   
4           7.50      0             12              17   35       0     1   

   south  manufacturing  construction  
0      0              1             0  
1      0              1             0  
2      0              1             0  
3      0              0             0  
4      0              0             0

In [2]: df.describe()
Out[2]: 
       wage_per_hour       union  education_yrs  experience_yrs         age  \
count     534.000000  534.000000     534.000000      534.000000  534.000000   
mean        9.024064    0.179775      13.018727       17.822097   36.833333   
std         5.139097    0.384360       2.615373       12.379710   11.726573   
min         1.000000    0.000000       2.000000        0.000000   18.000000   
25%         5.250000    0.000000      12.000000        8.000000   28.000000   
50%         7.780000    0.000000      12.000000       15.000000   35.000000   
75%        11.250000    0.000000      15.000000       26.000000   44.000000   
max        44.500000    1.000000      18.000000       55.000000   64.000000   

           female        marr       south  manufacturing  construction  
count  534.000000  534.000000  534.000000     534.000000    534.000000  
mean     0.458801    0.655431    0.292135       0.185393      0.044944  
std      0.498767    0.475673    0.455170       0.388981      0.207375  
min      0.000000    0.000000    0.000000       0.000000      0.000000  
25%      0.000000    0.000000    0.000000       0.000000      0.000000  
50%      0.000000    1.000000    0.000000       0.000000      0.000000  
75%      1.000000    1.000000    1.000000       0.000000      0.000000  
max      1.000000    1.000000    1.000000       1.000000      1.000000

# 6.