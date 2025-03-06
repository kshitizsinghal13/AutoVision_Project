from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai
from PIL import Image
import pyttsx3
from pyngrok import ngrok  
import base64  
from io import BytesIO  
import time

app = Flask(__name__)

IMAGE_DIR = 'captured_images'
LOG_FILE = 'responses.log'

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

DEFAULT_API_KEY = ""
DEFAULT_PROMPT = "Be concise Analyze the image and describe it as if you're guiding a blind friend. Provide essential navigation details and alert about any illegal, dangerous, or suspicious elements. Use an informal tone, be concise, and avoid repetition. If you notice any questions, provide solutions. If you see lyrics or references to a song, identify the song and artist. Mention any famous individuals, like political leaders or singers, you recognize. Keep it brief and to the point."



def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 200)
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def capture_and_analyze(apikey, prompt, image_path):
    genai.configure(api_key=apikey)
    generation_configuration = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
    }
    model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest", generation_config=generation_configuration, safety_settings=None)
    
    image = Image.open(image_path)
    response = model.generate_content([prompt, image])
    
    result = response.text
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    

    image_data = data.get('image_data')

    if not image_data:
        return jsonify({'error': 'Image data is required'}), 400
    
    image_data = image_data.split(",")[1]  
    image_bytes = Image.open(BytesIO(base64.b64decode(image_data)))

    # Generate a unique filename based on the current timestamp
    timestamp = int(time.time())
    temp_image_path = os.path.join(IMAGE_DIR, f'captured_image_{timestamp}.png')
    image_bytes.save(temp_image_path)

    # Analyze the image and get the result
    result = capture_and_analyze(DEFAULT_API_KEY, DEFAULT_PROMPT, temp_image_path)

    # Log the response to a text file
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"Image: {temp_image_path}, Result: {result}\n")

    return jsonify({'result': result})

if __name__ == '__main__':
    port = 5000
    
    # Connect ngrok using your static domain
    public_url = ngrok.connect(port, domain='marmot-clever-correctly.ngrok-free.app').public_url  
   
    print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")
    
    app.run(port=port)
