import questionary
import torch
from diffusers import FluxPipeline

from cache import read_cache, write_cache


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


def get_guidance_scale():
    # read the previously used guidance scale from the cache
    guidance_scale = read_cache().get("guidance_scale", 3.5)

    # pre-fill the guidance scale with the previous value
    guidance_scale = questionary.text(
        "Guidance Scale (float):", default=str(guidance_scale)
    ).ask()

    # cache the guidance scale for when the program is run the next time
    write_cache({"guidance_scale": guidance_scale})

    return float(guidance_scale)


def get_image_size():
    # read the previously used image size from the cache
    width = read_cache().get("width", 1024)
    height = read_cache().get("height", 1024)

    # pre-fill the width and height with the previous values
    width = questionary.text("Image Width (integer):", default=str(width)).ask()
    height = questionary.text("Image Height (integer):", default=str(height)).ask()

    # cache the width and height for when the program is run the next time
    write_cache({"width": width, "height": height})

    return int(width), int(height)


def get_prompt():
    # ask the user if want to pre-fill the prompt with the previous value
    prefill_prompt = questionary.confirm(
        "Do you want to pre-fill the prompt with the previous value?"
    ).ask()

    if prefill_prompt:
        # read the previously used prompt from the cache
        prompt = read_cache().get("prompt", "")

        # pre-fill the prompt with the previous value
        prompt = questionary.text("Image description:", default=prompt).ask()
    else:
        prompt = questionary.text("Enter the prompt for the image:").ask()

    # cache the prompt for when the program is run the next
    write_cache({"prompt": prompt})

    return prompt


def init():
    prompt = get_prompt()
    width, height = get_image_size()
    guidance_scale = get_guidance_scale()
    get_image(prompt, width, height, guidance_scale)
    print("Image generated.")


if __name__ == "__main__":
    init()
