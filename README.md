# AI-Powered Image Analyzer

This project is a Flask-based web application that allows users to upload images for analysis using Google's Generative AI. The application processes images and provides descriptions as if guiding a blind friend, while also detecting illegal, dangerous, or suspicious elements. It features voice output and logs all responses for future reference.

## Features
- Upload images for AI-based analysis
- Receive concise and meaningful descriptions
- Identify famous individuals, song lyrics, and references
- Provide navigation details for the visually impaired
- Store analysis logs for reference
- Convert results to speech output using pyttsx3
- Accessible remotely via Ngrok

## Technologies Used
- Python
- Flask
- Google Generative AI (Gemini 1.5 Flash)
- PIL (Pillow) for image processing
- Pyttsx3 for text-to-speech
- Pyngrok for remote access

## Installation and Setup
### Prerequisites
Ensure you have Python 3 installed along with the required dependencies.

### Clone the Repository
```sh
https://github.com/kshitizsinghal13/AutoVision_Project.git
cd AutoVision_Project
```

### Install Dependencies
```sh
pip install flask google-generativeai pillow pyttsx3 pyngrok
```

### Set API Key
Replace `DEFAULT_API_KEY` in the script with your Google Generative AI API key.

### Run the Application
```sh
python app.py
```

### Access via Ngrok
Ngrok will generate a public URL, which can be used to access the application remotely.

## Usage
1. Open the application in a web browser.
2. Upload an image for analysis.
3. View the generated response and listen to the text-to-speech output.
4. Check the `responses.log` file for stored results.

## File Structure
```
image-analyzer/
│── app.py            # Main application script
│── templates/
│   └── index.html    # Web interface template
│── captured_images/  # Directory for storing uploaded images
│── responses.log     # Log file for storing AI-generated responses
│── README.md         # Project documentation
```

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the project.

## Contact
For inquiries, reach out at kshitiz1303@gmail.com.
