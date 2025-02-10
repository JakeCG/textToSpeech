from pathlib import Path
from openai import OpenAI
from config import API_KEY


class TextToSpeechAPI:
    """
    Handles requests to OpenAI's text-to-speech API.
    """
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY)

    def text_to_speech(self, text, output_filename="output.mp3"):
        """
        Converts text to speech using OpenAI API and saves it as an MP3 file.
        """
        try:
            output_path = Path("output") / output_filename
            response = self.client.audio.speech.create(
                model="tts-1-hd",
                voice="coral",
                input=text,
            )
            response.stream_to_file(output_path)
            print(f"MP3 file saved: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None

