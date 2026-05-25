# services/docs_services.py
import io
import os
import torch
from PIL import Image
import torchvision.transforms as transforms
from dl.train_model import ResNet18, classes

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = ResNet18(num_classes=10)
weights_path = os.path.join("dl", "model_weights.pth")

try:
    model.load_state_dict(torch.load(weights_path, map_location=device, weights_only=True))
except FileNotFoundError:
    pass

model.to(device)
model.eval()

transform_test = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
])

def predict(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    tensor = transform_test(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(tensor)
        _, predicted = outputs.max(1)
        class_idx = predicted.item()

    return classes[class_idx]