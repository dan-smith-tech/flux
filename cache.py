"""
Reads and writes the `.input.json` file used to store the previous input of the user.

The cache should contain exactly:
- `prompt`: string - text prompt used to generate the image
- `width`: integer - width of the generated image
- `height`: integer - height of the generated image
- `guidance_scale`: integer - higher values result in closer adherence to the prompt
"""

import json


def read_cache():
    """
    Read the settings from the cache, ensuring only valid settings are returned.
    """

    try:
        with open(".input.json", "r", encoding="utf-8") as f:
            cache = {
                k: v
                for k, v in json.load(f).items()
                if v is not None
                and k in {"prompt", "width", "height", "guidance_scale"}
            }
    except FileNotFoundError:
        cache = {}

    return cache


def write_cache(settings):
    """
    Write the settings to the cache, ensuring only values passed into his function are written.
    """

    current_cache = read_cache()

    new_cache = current_cache.copy()
    new_cache.update({k: v for k, v in settings.items() if v is not None})

    if new_cache != current_cache:
        with open(".input.json", "w", encoding="utf-8") as f:
            json.dump(new_cache, f)
