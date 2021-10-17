import urllib

import torch
from PIL import Image
from torchvision import models, transforms

from app import config


def load_model():
    """Load pretrained DenseNet model and class labels."""
    model = torch.hub.load(
        config.PYTORCH_MODELS_REPO, config.DENSENET_NAME, pretrained=True
    )
    classes = [line.strip() for line in urllib.request.urlopen(config.CLASSES_URL)]
    return model, classes


model, classes = load_model()
# set model to inference mode
model.eval()


def infer(image_file):
    """Classify image."""
    preprocess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    with Image.open(image_file) as input_image:
        input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(
        0
    )  # create a mini-batch as expected by the model

    with torch.no_grad():
        output = model(input_batch)

    # get probabilities using softmax
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    # Show top categories per image
    top1_prob, top1_catid = torch.topk(probabilities, 1)
    return classes[top1_catid]
