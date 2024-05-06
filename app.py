from flask import Flask, render_template, request, send_file
import speech_to_text 
import text_to_speech
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/audio_to_text')
def audio_to_text():
    return render_template('audio_to_text.html')

@app.route('/text_to_audio')
def text_to_audio():
    return render_template('text_to_audio.html')

@app.route('/audio_to_text/upload', methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        if 'audioFile' not in request.files:
            return 'No file part'
        
        file = request.files['audioFile']

        if file.filename == '':
            return 'No selected file'
        
        filename = 'uploaded_file.wav'
        file.save(filename)

        transciption = speech_to_text.transcribe_audio(filename)

        return render_template('audio_to_text.html', result=transciption)
    return render_template('audio_to_text.html', result=None)

@app.route('/text_to_audio/upload_text', methods=['POST'])
def upload_text():
    text = request.form['textFile']
    
    audio = text_to_speech.text_to_speech(text)
    
   
    audio_file = 'output_audio.mp3'
    audio.save(audio_file)
    return send_file(audio_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)