from file_handler import FileHandler
from tts_api import TextToSpeechAPI


def main():
    file_handler = FileHandler()

    # Step 1: Read text from any available .docx file
    text = file_handler.read_file()

    if not text:
        print("No text extracted. Exiting program.")
        return

    print("Extracted Text:\n", text)

    # Step 2: Convert text to speech using OpenAI's API
    tts_api = TextToSpeechAPI()
    mp3_path = tts_api.text_to_speech(text)

    if mp3_path:
        print(f"MP3 file successfully generated at: {mp3_path}")
    else:
        print("Failed to generate MP3 file.")


if __name__ == "__main__":
    main()
