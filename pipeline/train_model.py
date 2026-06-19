import torch
import torch.nn as nn
import torch.optim as optim
from pipeline.prepare_gnn_data import X_tensor, Y_tensor
from pipeline.gnn_model import AdaptGenNet

# 1. Model Initialization
input_size = X_tensor.shape[1]
model = AdaptGenNet(input_dim=input_size)

# 2. Loss function aur Optimizer
criterion = nn.MSELoss()  # Regression task ke liye MSE best hai
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Training Loop
print("--- 🚀 Training shuru ho rahi hai... ---")
model.train()

for epoch in range(100):  # 100 baar data par process hoga
    # Zero gradients
    optimizer.zero_grad()
    
    # Forward pass: model predict karega
    outputs = model(X_tensor)
    
    # Loss calculate karein
    loss = criterion(outputs, Y_tensor)
    
    # Backward pass: seekhna (learning)
    loss.backward()
    optimizer.step()
    
    # Har 10th epoch par progress dikhayein
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

print("--- ✅ Training khatam ho gayi! ---")