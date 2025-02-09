"""
Downloads, configures, and runs the image generator model.

Modified version of https://gist.github.com/sayakpaul/23862a2e7f5ab73dfdcc513751289bea?permalink_comment_id=5141692#gistcomment-5141692
"""

import gc
import os

import torch
from diffusers import DiffusionPipeline
from transformers import T5EncoderModel


def flush():
    gc.collect()
    torch.cuda.empty_cache()


class FluxSchnell:
    """
    Modified version of:
    """

    def __init__(self):
        self.cache_dir = f"{os.getcwd()}/cache"

        self.t5_encoder = T5EncoderModel.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",
            subfolder="text_encoder_2",
            revision="refs/pr/7",
            torch_dtype=torch.bfloat16,
            cache_dir=self.cache_dir,
        )

        self.text_encoder = DiffusionPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",
            text_encoder_2=self.t5_encoder,
            transformer=None,
            vae=None,
            revision="refs/pr/7",
            cache_dir=self.cache_dir,
        )

        self.pipeline = DiffusionPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",
            torch_dtype=torch.bfloat16,
            revision="refs/pr/1",
            text_encoder_2=None,
            text_encoder=None,
            cache_dir=self.cache_dir,
        )

        self.pipeline.enable_model_cpu_offload()

    @torch.inference_mode()
    def inference(
        self, prompt, num_inference_steps=4, guidance_scale=0.0, width=1024, height=1024
    ):
        flush()

        self.text_encoder.to("cuda")
        (
            prompt_embeds,
            pooled_prompt_embeds,
            _,
        ) = self.text_encoder.encode_prompt(
            prompt=prompt, prompt_2=None, max_sequence_length=256
        )
        self.text_encoder.to("cpu")

        flush()

        output = self.pipeline(
            prompt_embeds=prompt_embeds.bfloat16(),
            pooled_prompt_embeds=pooled_prompt_embeds.bfloat16(),
            width=width,
            height=height,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
        )
        image = output.images[0]
        return image


def generate_image(model, prompt, width, height, guidance_scale, inference_steps):
    """
    (Down)Load the Flux and generate an image based on the provided prompt and settings.
    """

    image = model.inference(
        prompt=prompt,
        num_inference_steps=inference_steps,
        guidance_scale=guidance_scale,
        width=width,
        height=height,
    )
    return image
