# Create a Notetaking App with Speech Recognition

## Installation

On Mac you also need:
```
$ brew install portaudio
$ pip install pyobjc

```

Then use:
```
# pip install pyaudio
# pip install speechrecognition
# pip install requests gtts playsound
```

Note: On a M1 Mac you may need to use this command to install pyaudio
```
# python -m pip install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include' --global-option='-L/opt/homebrew/Cellar/portaudio/19.7.0/lib' pyaudio
```

For more setup instructions also have a look here:
- [Pyaudio Installation](http://people.csail.mit.edu/hubert/pyaudio/)
- [Speech Recognition](https://github.com/Uberi/speech_recognition)
- [Notion API setup](https://developers.notion.com/docs/getting-started)