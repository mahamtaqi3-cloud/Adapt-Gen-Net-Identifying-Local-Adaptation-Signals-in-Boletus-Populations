import torch
import torch.nn as nn
import torch.optim as optim
from pipeline.prepare_gnn_data import X_tensor, Y_tensor
from pipeline.gnn_model import AdaptGenNet

# 1. Model Initialization
input_size = X_tensor.shape[1]
model = AdaptGenNet(input_dim=input_size)

# 2. Loss function and Optimizer
criterion = nn.MSELoss()  # MSE is best for Regression task 
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Training Loop
print("--- 🚀 Training is starting... ---")
model.train()

for epoch in range(100):  # Processed for 100 times
    # Zero gradients
    optimizer.zero_grad()
    
    # Forward pass: model will predict
    outputs = model(X_tensor)
    
    # Calculate loss
    loss = criterion(outputs, Y_tensor)
    
    # Backward pass: (learning)
    loss.backward()
    optimizer.step()
    
    # Progress at every 10th epoch
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

print("--- ✅ Training finished! ---")
