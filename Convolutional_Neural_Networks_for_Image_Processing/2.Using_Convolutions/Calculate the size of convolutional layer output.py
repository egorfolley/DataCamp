'''
Zero padding and strides affect the size of the output of a convolution.

What is the size of the output for an input of size 256 by 256, with a kernel of size 4 by 4, padding of 1 and strides of 2?

'''

# Output_size = (input_size - kernel_size + 2 * padding) / strides + 1
print((256 - 4 + 2 * 1)/2 + 1) # 128