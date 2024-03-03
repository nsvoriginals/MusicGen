from .audiocraft.models import MusicGen
import torch
import streamlit as st

@st.cache
def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-melody')
    return model

def generate_music_tensors(description, duration: int):
    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    output = model.generate(
        descriptions=[description],
        progress=True,
        return_tokens=True
    )

    return output[0]
