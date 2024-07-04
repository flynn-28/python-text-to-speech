import argparse
from gtts import gTTS

def convert_text_to_speech(text, filename):
    tts = gTTS(text)
    tts.save(filename + ".mp3")
    print(f"Saved text to speech to {filename}")

def main():
    parser = argparse.ArgumentParser(description="MP3 Text To Speech")
    parser.add_argument("-t", "--text", type=str, required=True, help="defines spoken text")
    parser.add_argument("-n", "--name", type=str, required=True, help="defines name of output file")
    
    args = parser.parse_args()
    
    convert_text_to_speech(args.text, args.name)

if __name__ == "__main__":
    main()
