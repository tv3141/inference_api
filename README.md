# DenseNet App

Image classification app, based on DenseNet.

## Installation

```bash
make install-test
make test
```

```bash
make install
```

## Run App

```bash
densenet_api
```

The REST API uses multipart/form-data instead of base64 encoded JSON:
```bash
> curl --form 'image=@tests/images/cat.jpeg' http://127.0.0.1:5000/predict
{"response":"Persian cat"}
```

## Misc

The model and weights are loaded on first import from PyTorch repositories.

The inference code is based on [pytorch_vision_densenet](https://pytorch.org/hub/pytorch_vision_densenet/).
