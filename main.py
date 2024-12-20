"""
Entry point of the program.
"""

from input import (get_guidance_scale, get_image_size, get_output_file,
                   get_prompt)
from model import generate_image


def init():
    """
    Collect user input and generate an image accordingly.
    """

    prompt = get_prompt()
    width, height = get_image_size()
    guidance_scale = get_guidance_scale()
    output_file = f"output/{get_output_file()}.png"

    output_image = generate_image(prompt, width, height, guidance_scale)
    output_image.save(output_file)


if __name__ == "__main__":
    init()
