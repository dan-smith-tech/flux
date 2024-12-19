import questionary

from cache import read_cache, write_cache


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
