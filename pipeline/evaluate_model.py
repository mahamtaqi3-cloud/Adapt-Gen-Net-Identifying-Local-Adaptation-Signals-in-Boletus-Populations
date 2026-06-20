import torch
from pipeline.prepare_gnn_data import X_tensor, Y_tensor
from pipeline.gnn_model import AdaptGenNet
import os

# 1. Model Setup
input_size = X_tensor.shape[1]
model = AdaptGenNet(input_dim=input_size)

# 2. Load Trained Model 
# This will work when model will be saved in 'results' folder'
model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results', 'adapt_gen_model.pth')

if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path))
    print("--- ✅ Trained model successfully loaded! ---")
else:
    print("--- ⚠️ Model file not found, check after training. ---")

# 3. Evaluation
model.eval() # Put model in evaluation mode
with torch.no_grad():
    predictions = model(X_tensor)
    
    # Check loss
    criterion = torch.nn.MSELoss()
    loss = criterion(predictions, Y_tensor)
    
    print(f"\n--- 📈 Evaluation Results ---")
    print(f"Final Test Loss (MSE): {loss.item():.4f}")
    
    # Show some 
    print("\nSample Predictions vs Actual:")
    for i in range(min(5, len(Y_tensor))):
        print(f"Actual: {Y_tensor[i].item():.2f} | Predicted: {predictions[i].item():.2f}")

# Save model after training
os.makedirs('results', exist_ok=True)
torch.save(model.state_dict(), 'results/adapt_gen_model.pth')
print("--- ✅ Model is saved in 'results/adapt_gen_model.pth'! ---")
