'''
You've already trained a model that approximates the orbit of the meteor approaching earth and it's loaded for you to use.

Since you trained your model for values between -10 and 10 minutes, your model hasn't yet seen any other values for different time steps. You will visualize how your model behaves on unseen data.

To see the source code of plot_orbit, type the following print(inspect.getsource(plot_orbit)) in the console.

Remember np.arange(x,y) produces a range of values from x to y-1.

Hurry up, you're running out of time!

'''


# 1st task
# Predict the twenty minutes orbit
twenty_min_orbit = model.predict(np.arange(-10, 11))

# Plot the twenty minute orbit 
plot_orbit(twenty_min_orbit)


# 2st task
# Predict the eighty minute orbit
eighty_min_orbit = model.predict(np.arange(-40, 41))

# Plot the eighty minute orbit 
plot_orbit(eighty_min_orbit)