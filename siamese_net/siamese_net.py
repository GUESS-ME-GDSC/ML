from siamese_net.siameseNetwork import SiameseNetwork
from siamese_net.siameseNetworkDataset import SiameseNetworkDataset
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch
from torch.autograd import Variable
import torch.nn.functional as F

# Load trained model
model = SiameseNetwork().cuda()
model.load_state_dict(torch.load("siamese_model.pt"))

siamese_dataset = SiameseNetworkDataset(
    image1_path="/content/drive/MyDrive/siamese-net/content/sign_data/jeong/tmp2/dong1.jpeg",
    image2_path="/content/drive/MyDrive/siamese-net/content/sign_data/jeong/tmp2/dong2.jpeg",
    transform=transforms.Compose(
        [transforms.Resize((100, 100)), transforms.ToTensor()]
    ),
    should_invert=False,
)


test_dataloader = DataLoader(siamese_dataset, num_workers=6, batch_size=1, shuffle=True)
# dataiter = iter(test_dataloader)
# x0,_,_ = next(dataiter)

for i, data in enumerate(test_dataloader, 0):
    # _,x1,label2 = next(dataiter)
    x0, x1, label = data
    concatenated = torch.cat((x0, x1), 0)

    output1, output2 = model(Variable(x0).cuda(), Variable(x1).cuda())
    euclidean_distance = F.pairwise_distance(output1, output2)

    print("Dissimilarity: {:.2f}".format(euclidean_distance.item()))
