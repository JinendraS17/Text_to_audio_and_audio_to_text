import speech_recognition as sr

def transcribe_audio(filename):
    """
    Transcribe speech from an audio file using the Google Web Speech API.
    Parameters:
    - filename (str): The path to the audio file to be transcribed.
    Returns:
    - None: Prints the transcription of the audio to the console.
    """
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print('speed could be not be understood')
    except sr.RequestError as e:
        print('google wont process')

# filename = "output_2.wav"
# transcribe_audio(filename)

