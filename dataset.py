from torchvision import datasets
from torchvision import transforms

transform = transforms.ToTensor()  #converts 0->255 to 0->1

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)