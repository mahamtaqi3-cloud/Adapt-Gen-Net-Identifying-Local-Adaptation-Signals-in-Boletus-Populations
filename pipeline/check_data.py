import numpy as np
import os

# Check karein ki npy file mein kya hai
data = np.load('data/boletus_snp_matrix.npy')
print(f"Data shape: {data.shape}")
print(f"First 5 elements: {data[:5]}")