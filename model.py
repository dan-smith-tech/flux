import torch
from diffusers import FluxPipeline


def get_image(prompt, width, height, guidance_scale):
    # load the image generator model
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16
    )

    # run the model
    images = pipe(
        prompt,
        width=width,
        height=height,
        guidance_scale=guidance_scale,
        num_inference_steps=50,
        max_sequence_length=512,
    ).images

    # save each image to a file
    for i, image in enumerate(images):
        image.save(f"output-{i}.png")
