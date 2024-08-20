"""
https://github.com/rois-codh/kmnist
"""
import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)  # Fully connected layer (input: 28x28 pixels, output: 128 units)
        self.fc2 = nn.Linear(128, 64)       # Fully connected layer (input: 128 units, output: 64 units)
        self.fc3 = nn.Linear(64, 10)        # Fully connected layer (input: 64 units, output: 10 units for 10 classes)

    def forward(self, x):
        x = x.view(-1, 28 * 28)             # Flatten the input (batch_size, 1, 28, 28) -> (batch_size, 784)
        x = torch.relu(self.fc1(x))         # Apply ReLU activation function
        x = torch.relu(self.fc2(x))         # Apply ReLU activation function
        x = self.fc3(x)                     # Output layer (no activation function here)
        return x

def get_model(device):

    net = SimpleNN().to(device)
    model_path = "simple_nn.pth"
    if os.path.exists(model_path):
        if os.path.isfile(model_path):
            net.load_state_dict(torch.load(model_path, weights_only=True))
            return net
    train(epochs=1, model=net, hw=device)
    torch.save(net.state_dict(), 'simple_nn.pth')
    return net

def train(epochs, model, hw):
    # Define a transform to normalize the data

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    model.train()
    train_set = torchvision.datasets.KMNIST(root='./kdata', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)
    for epoch in range(epochs):
        for batch_idx, (input, target) in enumerate(train_loader):
            input, target = input.to(hw), target.to(hw)
            optimizer.zero_grad()
            output = model(input)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            if batch_idx % 100 == 0:
                print(f"Train Epoch: {epoch} [{batch_idx * len(input)}/{len(train_loader.dataset)} ({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}")


transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])


testset = torchvision.datasets.KMNIST(root='./kdata', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = get_model(device)
train(epochs=1, model=net, hw=device)
correct = 0
total = 0
with torch.no_grad():  # Disable gradient calculation for inference
    for data in testloader:
        images, labels = data
        images, labels = images.to(device), labels.to(device)
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy of the network on the 10000 test images: {100 * correct / total:.2f}%")


