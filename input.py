"""
Collects and processes user input.
"""

import questionary

from cache import read_cache, write_cache


def get_prompt():
    """
    Ask the user to enter a prompt for the image.

    Returns:
        str: The prompt entered by the user.
    """

    # ask the user if want to pre-fill the prompt with the previous value
    prefill_prompt = questionary.confirm(
        "Do you want to pre-fill the prompt with the previous value?"
    ).ask()

    if prefill_prompt:
        # read the previously used prompt from the cache, if available
        prompt = read_cache().get("prompt", "")

        # pre-fill the prompt with the previous value
        prompt = questionary.text("Image description:", default=prompt).ask()
    else:
        # ask the user to enter a new prompt
        prompt = questionary.text("Enter the prompt for the image:").ask()

    # cache the prompt for when the program is next run
    write_cache({"prompt": prompt})

    return prompt


def get_image_size():
    """
    Ask the user to enter the width and height of the image.

    Returns:
        tuple: A tuple containing the width and height of the image.
    """

    # read the previously used image size from the cache, if available
    width = read_cache().get("width", 1024)
    height = read_cache().get("height", 1024)

    # pre-fill the width and height with the previous values
    width = questionary.text("Image Width (integer):", default=str(width)).ask()
    height = questionary.text("Image Height (integer):", default=str(height)).ask()

    # cache the width and height for when the program is next run
    write_cache({"width": width, "height": height})

    return int(width), int(height)


def get_guidance_scale():
    """
    Ask the user to enter the guidance scale for the image.

    Returns:
        float: The guidance scale entered by the user.
    """

    # read the previously used image size from the cache, if available
    guidance_scale = read_cache().get("guidance_scale", 3.5)

    # pre-fill the width and height with the previous values
    guidance_scale = questionary.text(
        "Guidance scale (float):", default=str(guidance_scale)
    ).ask()

    # cache the width and height for when the program is next run
    write_cache({"guidance_scale": guidance_scale})

    return float(guidance_scale)


def get_inference_steps():
    """
    Ask the user to enter the number of inference steps for the image.

    Returns:
        int: The number of inference steps entered by the user.
    """

    # read the previously used image size from the cache, if available
    inference_steps = read_cache().get("inference_steps", 4)

    # pre-fill the width and height with the previous values
    inference_steps = questionary.text(
        "Inference Steps (integer):", default=str(inference_steps)
    ).ask()

    # cache the width and height for when the program is next run
    write_cache({"inference_steps": inference_steps})

    return int(inference_steps)


def get_num_images():
    """
    Ask the user to enter the number of images to generate.

    Returns:
        int: The number of images entered by the user.
    """

    # read the previously used image size from the cache, if available
    num_images = read_cache().get("num_images", 4)

    # pre-fill the width and height with the previous values
    num_images = questionary.text(
        "Number of images (integer):", default=str(num_images)
    ).ask()

    # cache the width and height for when the program is next run
    write_cache({"num_images": num_images})

    return int(num_images)


def get_running():
    """
    Ask the user if they want to continue running the program.

    Returns:
        bool: True if the user wants to continue running the program, False otherwise.
    """

    return questionary.confirm("Do you want to generate more images?").ask()
