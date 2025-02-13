# Oumi_LLM
This is a tutorial for oumi (*open universal machine intelligence*: a open-source platform that streamlines the entire lifecycle of foundation models - from data preparation and training to evaluation and deployment. )

## Installation

```shell
conda create -n oumi python=3.12
conda activate oumi
pip install oumi[gpu] (on linux machine wih nvidia gpu) / 
pip install oumi (on mac)
```

## Training a Model

Oumi spports for both custom and out-of-box models/ (models on HuggingFace and your own custom Pytorch model)

**Oumi uses training config files to specify training parameters.**

Training Configs: https://oumi.ai/docs/en/latest/api/oumi.core.configs.html#oumi.core.configs.TrainingConfig