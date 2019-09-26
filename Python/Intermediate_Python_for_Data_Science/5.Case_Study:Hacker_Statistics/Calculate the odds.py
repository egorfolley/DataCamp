'''
The histogram of the previous exercise was created from a Numpy array ends, that contains 500 integers. Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, the total number of simulations.

Well then, what's the estimated chance that you'll reach 60 steps high if you play this Empire State Building game? The ends array is everything you need; it's available in your Python session so you can make calculations in the IPython Shell.

'''

import numpy as np

np.random.seed(123)

ends = np.array([ 70,  94,  82,  66, 107,  49,  72, 116,  65,  78,  87,  47,  81,
        75,  56,  70,  77,  88,  55,  42,  74,  64,  63,  58,  70,  55,
        93,  98,  58,  60,  70,  70,  72,  71,  47,  78,  78,  79,  71,
        83,  71,  56,  63,  94,  49,  72,  63,  74,  61,  61,  79,  91,
        46,  66,  70,  55,   0,  80,  45,  89,  91,  61,  83,  71,  60,
        68,  74,  85,  68,  88,  64,  84, 114,  61,  65,  78,  63,  61,
        90,  96,  83,  77,  80,  71,  87,  73,  60,  85,  84,  76, 105,
        57,  98,  46,  63, 112,  81,  45, 101,  74,  77,  13,  81,  47,
        97,  90,  66,  52,  63,  54,  91,  26, 101,  81,  64,  95,  83,
        99,  75,  75,  61,  97,  57,  94,  76,  82,  86,  52, 122, 110,
        91,  47,  34,  94, 106,  58,  74,  75,  93,  64,  57,  76, 100,
        66,  98,  94,  60,  72,  55,  85,  66,  69,  59,  78,  81,  87,
        75,  58,  80,  97,  75,  67,  22,   6,  78,  87,  87,  80,  80,
       108,  59,  83,  76,  60,  73,  75,   8, 116,  10, 106,  78,  76,
        53, 103,  42,  49, 101,  80,  73,  66,  93,  92,  63,  89,  59,
        50,  57,  72,  41,  94,  79,  63,  88, 109,  88,  95,  52,  74,
        70,  80,  89,  77,  42,  83,  72,  65,  87,  80,  59,  67,  65,
        70,  86, 104,  69,  76,  76,  13,  39,  64,  57, 102,  66,  71,
        73,   2,  83,  75,  71,  84,  66,  79,  73,  56,  76,  84,  54,
        73,  57,  99,  69,  83,  33,  86,  81,  55,  77, 100,  87,  52,
        75,  58,  80,  98,  64,  75,  77,  58,  62,  98,  57,  89,   7,
        49,  66,  88, 108,  71,  32,  56,  54, 116,  87,  63,  88,  77,
       107,  67,  67,  71,  78,  64, 108,  24,  93, 100,  65,  97,  74,
        70,  79,  59,  66,  82,  87,  71,  43,  86,  68,  80,  50,  61,
        67,  43,  59,  31,  31,  69,  60, 110,  57,  95,  63,  56, 117,
        72,  71,  99,  72,  81,  69,   2,  28, 103,  89,  63,  61,  54,
        78,  65,  64,  84,  31,  85,  69,  65,  77,  38,  70,  89,  58,
        78,  43,  69,  69,  14,  81, 107,  70,  52,  55,  41,  83,  90,
        94,  63,  46, 101,  82,  76,  84,  91,  79,  83,  94,  73,  71,
        67,  95,  68,  97,  95,  12,  72,  75,  78,  93,  87,  71,  10,
        74,  22,  70,  48,  92,  81,  90,  73,  66,  97,  76,  64, 100,
        76,  58,  94,  80,  63,  71,  41,  86,  81,  95,  64,  69,  25,
        69,  87,  64,  93,  82,  89,  51,  68,   5,  82,  75,  74,  82,
       101,  75,  49,  60,  89,  61,  68,  32,  72,  54,  70,  51,  46,
        40,  77,  83,  81,  85,  91,  73,  52,  80,  70,  38, 127,  60,
       110,  77,  56,  82,  88,  98,  86,  67,  66,  60,  72,  92,  75,
       109,  61,  78,  77,  98,  62,  67,  68,  69,  46,  65,  96,  67,
        91,  95,  71,  86,  84,  73,  73,  67,  62,  38,  69,  76,  78,
        88,  80,  80,  91,  57,  65])

print(float(np.count_nonzero(ends >= 60))/500)
# 78.4 %
