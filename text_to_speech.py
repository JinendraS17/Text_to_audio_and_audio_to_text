from gtts import gTTS

def text_to_speech(text):
    """
    Convert input text into speech using Google Text-to-Speech (gTTS) library.
    Parameters:
    - text (str): The input tex to be converted into speech
    - lang (str): defult en

    Returns:
    - audio_output_encoded: an audio obkect represnting the speech generated from the input text.
    """
    audio_ouput_encoded = gTTS(text=text, lang='en', slow=False)
    return audio_ouput_encoded

# try:
#     text = "Welcome to Setoo Solutions. Setoo is niche design-led technology solution company. A team of experts to link your business ideas to the web and bring them to life. We are all about providing the technology solutions throughout the product life cycle."
#     audio_output_decoded = text_to_speech(text)
#     if audio_output_decoded:
#         audio_output_decoded.save('output.wav')
#         print("Speech generated successfully!")
# except TypeError as e:
#     print("Error: ", e)

