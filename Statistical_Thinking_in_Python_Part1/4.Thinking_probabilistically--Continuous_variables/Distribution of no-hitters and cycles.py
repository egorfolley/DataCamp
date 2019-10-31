'''
Distribution of no-hitters and cycles
Now, you'll use your sampling function to compute the waiting time to observe a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean waiting time for hitting the cycle is 715 games.

'''


# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, 10 ** 5)

# Make the histogram
plt.hist(waiting_times, bins=100, normed=True, histtype='step')

# Label axes
plt.xlabel('time')
plt.ylabel('PDF')

# Show the plot
plt.show()