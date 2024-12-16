"""
A `.input.json` file is used to store the previously used setup of the model

This file should contain:
- `prompt` : string - text prompt used to generate the image
- `width` : integer - width of the generated image
- `height` : integer - height of the generated image
- `guidance_scale` : integer - higher values result in closer adherence to the prompt
"""

import json


def read_cache():
    """
    Read the settings from the `.input.json` file.
    """

    try:
        with open(".input.json", "r", encoding="utf-8") as f:
            settings = {
                k: v
                for k, v in json.load(f).items()
                if v is not None
                and k in {"prompt", "width", "height", "guidance_scale"}
            }
    except FileNotFoundError:
        settings = {}

    return settings


def write_cache(settings):
    """
    Write the settings to the `.input.json` file
    """

    # get current cache
    new_settings = read_cache()

    # update the cache with only the settings that are not None and that are inside the passed in settings
    new_settings.update({k: v for k, v in settings.items() if v is not None})

    # TODO: do not write if there is no diff

    with open(".input.json", "w", encoding="utf-8") as f:
        json.dump(new_settings, f)
