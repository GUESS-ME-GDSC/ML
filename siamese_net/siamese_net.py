from siamese_net.siameseNetworkDataset import SiameseNetworkDataset
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch
from torch.autograd import Variable
import torch.nn.functional as F

# Load trained model
model = SiameseNetworkDataset().cuda()
model.load_state_dict(torch.load("siamese_model.pt"))

# folder_dataset_test = dset.ImageFolder(root=Config.testing_dir)
folder_dataset_test = dset.ImageFolder(
    root="/content/drive/MyDrive/siamese-net/content/sign_data/jeong"
)

siamese_dataset = SiameseNetworkDataset(
    imageFolderDataset=folder_dataset_test,
    transform=transforms.Compose(
        [transforms.Resize((100, 100)), transforms.ToTensor()]
    ),
    should_invert=False,
)


test_dataloader = DataLoader(siamese_dataset, num_workers=6, batch_size=1, shuffle=True)

dataiter = iter(test_dataloader)
x0, _, _ = next(dataiter)

for i in range(10):
    _, x1, label2 = next(dataiter)
    concatenated = torch.cat((x0, x1), 0)

    output1, output2 = model(Variable(x0).cuda(), Variable(x1).cuda())
    euclidean_distance = F.pairwise_distance(output1, output2)

    print("Dissimilarity: {:.2f}".format(euclidean_distance.item()))
