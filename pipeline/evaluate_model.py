import torch
from pipeline.prepare_gnn_data import X_tensor, Y_tensor
from pipeline.gnn_model import AdaptGenNet
import os

# 1. Model Setup
input_size = X_tensor.shape[1]
model = AdaptGenNet(input_dim=input_size)

# 2. Trained Model Load Karein
# Yeh tabhi chalega agar 'results' folder mein model save hai
model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results', 'adapt_gen_model.pth')

if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path))
    print("--- ✅ Trained model successfully loaded! ---")
else:
    print("--- ⚠️ Model file nahi mili, training ke baad check karein. ---")

# 3. Evaluation
model.eval() # Model ko evaluation mode mein daalein
with torch.no_grad():
    predictions = model(X_tensor)
    
    # Loss check karein
    criterion = torch.nn.MSELoss()
    loss = criterion(predictions, Y_tensor)
    
    print(f"\n--- 📈 Evaluation Results ---")
    print(f"Final Test Loss (MSE): {loss.item():.4f}")
    
    # Kuch predictions dikhayein
    print("\nSample Predictions vs Actual:")
    for i in range(min(5, len(Y_tensor))):
        print(f"Actual: {Y_tensor[i].item():.2f} | Predicted: {predictions[i].item():.2f}")

# Training khatam hone ke baad model save karein
os.makedirs('results', exist_ok=True)
torch.save(model.state_dict(), 'results/adapt_gen_model.pth')
print("--- ✅ Model 'results/adapt_gen_model.pth' mein save ho gaya! ---")