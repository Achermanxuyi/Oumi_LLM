import os
from pathlib import Path

tutorial_dir = "tour_tutorial"

Path(tutorial_dir).mkdir(parents=True, exist_ok=True)
os.environ["TOJENIZERS_PARALLELISM"] = "false" # Dsable warning from HF


'''
Training a model, Oumi supports training both custom and out-of-the-box models.
Training existing model from HuggingFace: SmolLM2 135M, as the model is small and trains quickly
'''

yaml_content = f"""
model:
  model_name: "HuggingFaceTB/SmolLM2-135M-Instruct"
  torch_dtype_str: "bfloat16"
  trust_remote_code: True

data:
  train:
    datasets:
      - dataset_name: "yahma/alpaca-cleaned"
    target_col: "prompt"

training:
  trainer_type: "TRL_SFT"
  per_device_train_batch_size: 2
  max_steps: 10 # Quick "mini" training, for demo purposes only.
  run_name: "smollm2_135m_sft"
  output_dir: "{tutorial_dir}/output"
"""

with open(f"{tutorial_dir}/train.yaml", "w") as f:
    f.write(yaml_content)
    
    
