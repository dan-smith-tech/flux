"""
Downloads, configures, and runs the image generator model.
"""

import torch
from diffusers import FluxPipeline


def generate_image(prompt, width, height, guidance_scale):
    """
    (Down)Load the Flux and generate an image based on the provided prompt and settings.
    """

    # (down)load the image generator model
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16
    )

    # run the model and return the generated image
    return pipe(
        prompt,
        width=width,
        height=height,
        guidance_scale=guidance_scale,
        num_inference_steps=50,
        max_sequence_length=512,
    ).images[0]
