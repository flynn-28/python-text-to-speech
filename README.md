# Text To Speech

## Requirements
1. gTTS: `pip install gTTS`

## Usage
`usage: tts.py [-h] -t "TEXT" -n NAME`
Example command: `python3 -m tts -t "Hello, World!" -n hello`
Flags: 
 1. `-t` Specify the text to be spoken
 2. `-n` the name of the output file
 
## Windows Binary
Available [here](https://github.com/flynn-28/python-text-to-speech/releases/download/windows/windows-tts.zip)
 
### Usage
`usage: tts.exe [-h] -t "TEXT" -n NAME`
Example command: `tts.exe -t "Hello, World!" -n hello`
Flags: 
 1. `-t` Specify the text to be spoken
 2. `-n` the name of the output file
