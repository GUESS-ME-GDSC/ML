import torchvision.transforms as transforms
import torch
import torch.nn.functional as F
import cv2
from url_to_image import url_to_image
from siamese_net.siameseNetwork import SiameseNetwork


def checkSimilarity(path1, path2):
    # Load trained model
    model = SiameseNetwork().cuda()
    model.load_state_dict(torch.load("siamese_model.pt"))

    # read the images online
    img1 = url_to_image(path1)
    img2 = url_to_image(path2)

    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # resize images for comparison
    img1 = cv2.resize(img1, (100, 100))
    img2 = cv2.resize(img2, (100, 100))

    img1_tensor = transforms.ToTensor()(img1)
    img2_tensor = transforms.ToTensor()(img2)

    # move the tensors to the desired device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    img1_tensor = img1_tensor.to(device)
    img2_tensor = img2_tensor.to(device)

    img1_tensor = torch.unsqueeze(img1_tensor, 0)  # Add batch dimension to img1_tensor
    img2_tensor = torch.unsqueeze(img2_tensor, 0)

    output1, output2 = model(img1_tensor, img2_tensor)
    euclidean_distance = F.pairwise_distance(output1, output2)

    return "Dissimilarity: {:.2f}".format(euclidean_distance.item())
