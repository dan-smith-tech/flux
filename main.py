"""
Entry point of the program.
"""

from accelerate.utils.dataclasses import os
from accelerate.utils.modeling import tempfile

from input import (get_guidance_scale, get_image_size, get_inference_steps,
                   get_num_images, get_prompt, get_running)
from model import FluxSchnell, generate_image


def init():
    """
    Collect user input and generate an image accordingly.
    """

    print("Setting up model pipeline...")
    model = FluxSchnell()

    running = True
    while running:
        print("")
        prompt = get_prompt()
        width, height = get_image_size()
        guidance_scale = get_guidance_scale()
        inference_steps = get_inference_steps()
        num_images = get_num_images()
        print("Generating images...")

        with tempfile.TemporaryDirectory() as temp_dir:
            for i in range(num_images):
                image = generate_image(
                    model, prompt, width, height, guidance_scale, inference_steps
                )
                image_path = os.path.join(temp_dir, f"image_{i}.png")
                image.save(image_path)

            os.system(f"feh {temp_dir}/*")

        running = get_running()


if __name__ == "__main__":
    init()
