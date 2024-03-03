import streamlit as st
from logic import model_logic, audio_logic, file_logic

st.set_page_config(
    page_icon="musical_note",
    page_title="Music Gen"
)

def main():
    st.title("Text to Music Generator🎵")

    with st.expander("See explanation"):
        st.write("Music Generator app built using Meta's Audiocraft library. We are using Music Gen Small model.")

    text_area = st.text_area("Enter your description.......")
    time_slider = st.slider("Select time duration (In Seconds)", 0, 20, 10)

    if text_area and time_slider:
        st.json({
            'Your Description': text_area,
            'Selected Time Duration (in Seconds)': time_slider
        })

        st.subheader("Generated Music")
        music_tensors = model_logic.generate_music_tensors(text_area, time_slider)
        audio_logic.save_audio(music_tensors)
        audio_filepath = 'audio_output/audio_0.wav'
        audio_bytes = open(audio_filepath, 'rb').read()
        st.audio(audio_bytes)
        st.markdown(file_logic.get_binary_file_downloader_html(audio_filepath, 'Audio'), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
