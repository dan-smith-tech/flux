"""
Collects and processes user input.
"""

import questionary

from cache import read_cache, write_cache


def get_output_file():
    """
    Ask the user to enter the name of the output file.

    Returns:
        str: The name of the output file entered by the user.
    """

    # read the previously used output file from the cache, if available
    output_file = read_cache().get("output_file", "output")

    # pre-fill the output file with the previous value
    output_file = questionary.text(
        "Output Filename (/output/<this_value>.png):", default=output_file
    ).ask()

    # cache the output file for when the program is next run
    write_cache({"output_file": output_file})

    return output_file


def get_guidance_scale():
    """
    Ask the user to enter a guidance scale.

    Returns:
        float: The guidance scale entered by the user.
    """

    # read the previously used guidance scale from the cache, if available
    guidance_scale = read_cache().get("guidance_scale", 3.5)

    # pre-fill the guidance scale with the previous value
    guidance_scale = questionary.text(
        "Guidance Scale (float):", default=str(guidance_scale)
    ).ask()

    # cache the guidance scale for when the program is next run
    write_cache({"guidance_scale": guidance_scale})

    return float(guidance_scale)


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
