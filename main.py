from input import get_guidance_scale, get_image_size, get_prompt

# from model import get_image


def init():
    prompt = get_prompt()
    width, height = get_image_size()
    guidance_scale = get_guidance_scale()
    # get_image(prompt, width, height, guidance_scale)
    # print("Image generated.")
    print("Prompt: ", prompt)
    print("Width: ", width)
    print("Height: ", height)
    print("Guidance Scale: ", guidance_scale)


if __name__ == "__main__":
    init()
